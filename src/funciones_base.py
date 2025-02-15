import threading

def timeout_input(prompt, timeout):
    user_input = [None]
    def get_input():
        user_input[0] = input(prompt)
    
    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        print("Tiempo excedido")
        return None
    return user_input[0]


def test_threading():
    print("Threading module is available")

test_threading()