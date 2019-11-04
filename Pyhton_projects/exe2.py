from tkinter import *
import matplotlib.pyplot as plt

###read!!!! the graph in the right side near to scrView->>>>
#ten words that first appear in the file
# 2-b
def crate_frequency():
    file1 = open("word.txt", 'r')
    list_str = []
    #create list with ten letter
    while len(list_str) < 10:
        string1 =file1.read(10)
        if string1 is "":
            print("the file don't have more ten letter")
            file1.close()
            return -1
        for i in string1:
            if len(list_str) < 10:
                if i.lower() not in list_str and i.lower() >= 'a' and i.lower() <= 'z':
                    list_str.append(i)
    list_str.sort()
    list_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #create dict with the list any value represent position in for key(letter) to add
    dict_for_counter = dict(zip(list_str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    file1.seek(0)
    string1 = file1.readline()
    while string1 is not "":
        for i in string1:
            if i.lower() in list_str:
                list_counter[dict_for_counter[i.lower()]] += 1
        string1 = file1.readline()
    file1.close()
    plt.bar(list_str, list_counter, label="2-b")
    plt.legend()
    plt.xlabel('letter')
    plt.ylabel('bar Frequency in file')
    plt.title('Frequency of 10 digits of the beginning of the file')
    plt.show()


#2-a
class generator1:

    def __init__(self):
        self.generator_text = self.my_generator("e")

    def my_generator(self, char):
        bool = str(includeOrExclude.get())
        if bool.lower() == "e":
            check = 0
        else:
            check = 1
        with open("word.txt", "r") as file:
            txt = file.read()
            lines = txt.split("\n")
            for line in lines:
                new_line = re.split(',', line)
                for w in new_line:
                    if (char.lower() in w or char.upper() in w)and check == 1:
                        yield w
                    elif check == 0 and(char.lower() not in w and char.upper() not in w):
                        yield w

    def next_text(self):
        try:
            textOfGenerator.config(text=str(self.generator_text.__next__()))
        except StopIteration:
            textOfGenerator.config(text="end of generator!!!!")

    def start_begin(self):
        try:
            while True:
                self.generator_text.__next__()
        except StopIteration:
            self.__init__()

if __name__ == "__main__":
    #2-b
    generator1 = generator1()
    #2-a
    root = Tk()
    #frame
    frameGraph = Frame(root, bd="30")
    frameGraph.pack(side=BOTTOM)
    frameBuuton= Frame(root, bd="30")
    frameBuuton.pack(side=RIGHT)
    labelFrame = Frame(root, bd="30")
    labelFrame.pack(side=TOP)
    #graph
    GraphButton = Button(frameGraph, text="show graph", command=crate_frequency)
    GraphButton.grid(row=0, column=0)
    #label
    lable1 = Label(labelFrame, text="text read from generator: ")
    lable1.grid(row=0, column=0)
    textOfGenerator = Label(labelFrame, text="")
    textOfGenerator.grid(row=0, column=2)
    #button
    nextButton = Button(labelFrame, text="next", command=generator1.next_text)
    nextButton.grid(row=2, column=3)
    initButton = Button(frameBuuton, text="init generator", command=generator1.start_begin)
    initButton.grid(row=1, column=1)
    #entry for include
    Label(frameBuuton, text="for Exclude:e else include ").grid(row=0, column=0)
    includeOrExclude = Entry(frameBuuton, text="")
    includeOrExclude.grid(row=0, column=1)
    Label(frameBuuton, text="for replace include or  Exclude press init").grid(row=2, column=0)
    root.mainloop()