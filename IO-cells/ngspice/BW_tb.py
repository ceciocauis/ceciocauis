import subprocess
import readline



def change_testbench(archivo_test):
    
    with open("BW_tb.spice", "r") as file:
        lines = file.readlines() # saves all file lines as a list.
            
        for i, line in enumerate(lines):
            if (".include") in line:
                lines[i] = ".include "+whole_file+".spice\n"
            if ("wrdata") in line:
                lines[i] = "wrdata out_"+whole_file+".txt db(out)\n"

    with open("BW_tb.spice", "w") as file:
        file.writelines(lines) # write all list elements into the file.


readline.parse_and_bind('tab: complete')
whole_file = input("\nWrite Test to simulate [e.g Padtest_]: ")
whole_file = whole_file.replace(".spice","")

change_testbench(whole_file)
subprocess.run(["ngspice","BW_tb.spice"]) # run file
