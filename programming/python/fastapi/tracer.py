import sys
import threading

# A thread-local object to store the call depth for proper indentation
_trace_data = threading.local()

def simple_tracer(frame, event, arg):
    # We only care about the 'call' event
    if event == 'call':
        # Get function and module name
        func_name = frame.f_code.co_name
        module_name = frame.f_globals.get('__name__', '?')
        
        # --- The Filter ---
        # Only show functions from these specific modules
        if 'fastapi' in module_name or 'starlette' in module_name:
            # Calculate and print indentation based on call depth
            depth = getattr(_trace_data, 'depth', 0)
            print(f"{'  ' * depth}--> call: {module_name}.{func_name}")
            _trace_data.depth = depth + 1
            
    # As we return from a function, decrease the indent depth
    elif event == 'return':
        depth = getattr(_trace_data, 'depth', 0)
        if depth > 0:
            _trace_data.depth = depth - 1

    return simple_tracer