# main.py
from ... import ...

"""import the decorator and use it here then run this file"""

def hack_satellite(code_name):
    return f"Satellite hacked by {code_name}"


def steal_document(agent):
    return f"Documents stolen by agent {agent}"

def main():
    print(hack_satellite("ShadowFox"))
    print(steal_document("GhostWolf"))

if __name__ == "__main__":
    main()
