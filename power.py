power_cfg = open("/sys/class/power_supply/BAT0/charge_control_end_threshold", "r")
print("Current Charge Threshold:")

print(power_cfg.read())
power_cfg = open("/sys/class/power_supply/BAT0/charge_control_end_threshold", "w")
change_opt = input("Change? y/n: ")

if(change_opt == "y"):
    ch_val = input("Enter New Value: ")
power_cfg.write(ch_val)
