# src/tools/code_exec.py
# Very simple safe "executor" for quiz auto-grading (non-sandboxed).
# WARNING: executing untrusted code is dangerous. For production use a real sandbox.
def run_python_snippet(code_snippet, globals_dict=None):
    globals_dict = globals_dict or {}
    locals_dict = {}
    try:
        exec(code_snippet, globals_dict, locals_dict)
        return locals_dict
    except Exception as e:
        return {'error': str(e)}
