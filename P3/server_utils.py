import termcolor


def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip="False")
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping():
    print_colored("PING command", "green")

def get():
    slices = formatted.message.split(" ")
    if len(slices) == 2 and slices[0] == "GET":
        try:
            n = int(slices[1])
            if 0 <= n <= len(SEQUENCES_LIST):
                termcolor.cprint(f"GET", 'green')
                seq = SEQUENCES_LIST[n]
                termcolor.cprint(f"{seq}\n", 'white')
                cs.send(f"{seq}".encode())
                cs.close()
        except ValueError:
            pass
