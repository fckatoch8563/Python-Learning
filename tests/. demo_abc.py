# import sys


# def read_one_line():
#     # Interactive terminal: show prompt and use input()
#     if sys.stdin.isatty():
#         try:
#             line = input("Enter a line: ")
#         except EOFError:
#             print("No input (EOF).")
#             return
#     else:
#         # Non-interactive (pipe/heredoc): don't print prompt, read from stdin
#         line = sys.stdin.readline().rstrip("\n")
#         if not line:
#             print("No input (EOF).")
#             return
#     print("Got line:", line)


# if __name__ == "__main__":
#     read_one_line()
###################################################################################
