from tkinter import Tk
from interfaz.interfaz import Interfaz

def main():
    root = Tk()
    app = Interfaz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
