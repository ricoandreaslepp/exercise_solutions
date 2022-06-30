# /2021-12-05-ev kaustas
# peaks(?) töötama iga failiga

import os
import sys
import subprocess
import argparse
import time
import logging
from tqdm import tqdm as tq

# global variables
SCRIPT_NAME = None
AMOUNT = None # of testcases 
MAX_EXEC_TIME = None
DEBUG_MODE = None

LOGFILE = None

class term_colors:
	WRONG = '\033[91m'
	CORRECT = '\033[92m'
	ENDC = '\033[0m'

def setup_argparse():
	# SCRIPT_NAME is a mandatory argument, else are optional
	parser = argparse.ArgumentParser()

	arguments = [
		["-inf", "--infile", True, None, "input file", str],
		["-t", "--tests", False, None, "testcases", int], # run all cases if not specified
		["-T", "--time", False, 3, "max execution time", float], # possibly annoying..
		["-d", "--debug", False, False, "debug mode", bool],
	]

	for a in arguments:
		parser.add_argument(*a[:2], required=a[2], default=a[3], help=a[4], type=a[5])

	return parser.parse_args()

def setup_logs():
	open(LOGFILE, "w").close() # CLEAR LOGS FROM LAST RUN
	logging.basicConfig(
		filename=LOGFILE,
		level=logging.INFO, 
		format='[%(levelname)s] : %(message)s',
	)

def read_output():
	for i in range(AMOUNT+1):
		with open(f"./{SCRIPT_NAME}/output/output{i}.txt", "r") as outf:
			# failide võrdlemise asemel teeme outputid string repriks
			r = "".join(outf.readlines())
			yield r

# ------------------------------------------------------------------------------------
# VÕIB OLENEDA INPUTIST, nt järjekord jms
def compare(prog_output, correct_ans):
	if SCRIPT_NAME == "ratsu":
		return bool(sorted(prog_output)==sorted(correct_ans))

	return bool(prog_output==correct_ans)

# ------------------------------------------------------------------------------------
def run():
	fcnt = tcnt = max_runtime = 0
	output = read_output()

	for i in tq(range(AMOUNT+1)):
		# running actual codes
		start = time.perf_counter()

		r = subprocess.run(f"pypy3 ./{SCRIPT_NAME}/{SCRIPT_NAME}.py < ./{SCRIPT_NAME}/input/input{i}.txt", capture_output=True, shell=True)
		prog_out = r.stdout.decode()

		took = time.perf_counter()-start
		
		correct = next(output)

		if DEBUG_MODE:
			print("[DEBUG] CODE OUTPUT")
			for line in prog_out:
				print(line, end="")

			print("vastus:")
			for line in correct:
				print(line, end="")

		result = compare(prog_out, correct)

		tcnt += bool(result and took <= MAX_EXEC_TIME)
		fcnt += not bool(result and took <= MAX_EXEC_TIME)
		max_runtime = max(max_runtime, took)

		if result and took <= MAX_EXEC_TIME:
			print(f"{term_colors.CORRECT}[+] input{i}.txt {term_colors.ENDC} {took} seconds")

		else:
			input_msg = f"{term_colors.WRONG}[T] {term_colors.CORRECT}input{i}.txt {term_colors.ENDC}" if result else f"{term_colors.WRONG}[?] input{i}.txt {term_colors.ENDC}"
			time_msg = f"{term_colors.CORRECT}" if took <= MAX_EXEC_TIME else f"{term_colors.WRONG}"
			full_msg = f"{input_msg}{time_msg}{took} seconds{term_colors.ENDC}"
			
			print(full_msg)
			logging.warning(f"input{i}.txt output: {prog_out} {took}")

	logging.info(f'''
		Correct: {tcnt} 
		Wrong: {fcnt} 
		Longest runtime: {max_runtime}''')
	print(f'''
	[+] Correct:\t{" ".join([term_colors.CORRECT, str(tcnt), term_colors.ENDC])}
	[-] Wrong:\t{" ".join([term_colors.CORRECT, str(fcnt), term_colors.ENDC]) if fcnt==0 else " ".join([term_colors.WRONG, str(fcnt), term_colors.ENDC])}
	[T] Time:\t{" ".join([term_colors.CORRECT, str(max_runtime), term_colors.ENDC]) if max_runtime <= 3 else " ".join([term_colors.WRONG, str(max_runtime), term_colors.ENDC])}''')

if __name__=="__main__":
	args = setup_argparse()

	# init global vars
	SCRIPT_NAME = args.infile
	max_inputs = max([int(_.replace("input","").replace(".txt", "")) for _ in subprocess.run(f"ls ./{SCRIPT_NAME}/input", shell=True, capture_output=True).stdout.decode().strip().split("\n")])
	AMOUNT = args.tests if args.tests and args.tests<max_inputs else max_inputs
	MAX_EXEC_TIME = args.time
	DEBUG_MODE = args.debug
	LOGFILE = f"./{SCRIPT_NAME}/{SCRIPT_NAME}.log"

	setup_logs()

	try:
		run()
	except (KeyboardInterrupt):
		pass
