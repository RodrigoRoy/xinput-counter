from XInput import *

# Counter variables for buttons
counter_A = 0
counter_B = 0
counter_X = 0
counter_Y = 0

# Reset the counters in files
with open('input_data/A_button.txt', 'w') as file:
    file.write(str(counter_A))
with open('input_data/X_button.txt', 'w') as file:
    file.write(str(counter_X))
with open('input_data/Y_button.txt', 'w') as file:
    file.write(str(counter_Y))
with open('input_data/B_button.txt', 'w') as file:
    file.write(str(counter_B))

while 1:
    events = get_events() # Using the Event-system
    for event in events:
        if event.type == EVENT_CONNECTED:
            print('Control connected');
        elif event.type == EVENT_DISCONNECTED:
            print('Control disconnected');

        elif event.type == EVENT_BUTTON_RELEASED:
            if event.button == "A":
                counter_A += 1;
                with open('input_data/A_button.txt', 'w') as file:
                    file.write(str(counter_A))
            elif event.button == "B":
                counter_B += 1;
                with open('input_data/B_button.txt', 'w') as file:
                    file.write(str(counter_B))
            elif event.button == "Y":
                counter_Y += 1;
                with open('input_data/Y_button.txt', 'w') as file:
                    file.write(str(counter_Y))
            elif event.button == "X":
                counter_X += 1;
                with open('input_data/X_button.txt', 'w') as file:
                    file.write(str(counter_X))
            print('A: {}, B: {}, X: {}, Y: {}'.format(counter_A, counter_B, counter_X, counter_Y))
