#!/usr/bin/env python3

import os
import sys
import psutil
import ijson
import functools
import time
import io
from contextlib import redirect_stdout


def capture_output(func):
    """returns {"value": value, "printout": captured_string}"""

    @functools.wraps(func)
    def wrapper_capture_output(*args, **kwargs):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            value = func(*args, **kwargs)

        captured_string = captured_output.getvalue()
        return {"value": value, "printout": captured_string}

    return wrapper_capture_output


def timer(func):
    """Print the runtime of the decorated function."""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        # Start the timer
        start_time = time.perf_counter()
        value = func(*args, **kwargs)

        # Calculate run time
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Finished {func.__name__!r} in {run_time:.4f} seconds.")
        return value

    return wrapper_timer


def trace_locals(func):
    """Trace local variables inside a function."""

    @functools.wraps(func)
    def wrapper_tracer(*args, **kwargs):
        def tracer(frame, event, arg):
            if event == "line" and frame.f_code == func.__code__:
                print(f"Line {frame.f_lineno} locals: {frame.f_locals}")
            return tracer

        original_trace = sys.gettrace()
        sys.settrace(tracer)
        try:
            result = func(*args, **kwargs)
        finally:
            sys.settrace(original_trace)
        return result

    return wrapper_tracer


def get_json_len(full_source_file_path: str) -> int:
    """Get the number of items i.e., dictionaries in file"""
    try:
        if os.path.isfile(full_source_file_path):
            with open(full_source_file_path, "rb") as fh:
                data_gen = ijson.items(fh, "item", use_float=True)
                n = len(list(data_gen))
                del data_gen
            fh.close()
            return n
    except Exception as e:
        raise Exception(e)


# https://www.geeksforgeeks.org/python/monitoring-memory-usage-of-a-running-python-program/


def process_memory():
    """inner psutil function for the profile wrapper"""
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def profile(func):
    """profile decorator function"""

    def wrapper_profile(*args, **kwargs):

        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print(
            "{}:consumed memory: {:,}".format(
                func.__name__, mem_before, mem_after, mem_after - mem_before
            )
        )

        return result

    return wrapper_profile
