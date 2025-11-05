import sys

EXIT_WORDS = {'exit', 'leave', 'quit', 'q'}
YES_WORDS = {'yes', 'y', 'yeah', 'yep', 'yeh', 'yup', 'correct', 'affirmative'}
NO_WORDS = {'no', 'nay', 'nope', 'n', 'nah'}

log = open('chatlog.txt', 'w', buffering=1)

def log_print(text=""):
    print(text)                     # show in terminal
    log.write(text + "\n")          # mirror to file for the web viewer
    log.flush()

def ask(prompt, valid=None):
    # Log to file for browser:
    log_print(prompt)

    while True:
        ans = input("> ").strip().lower()   # no prompt string here
        log.write(f"> {ans}\n")

        if ans in EXIT_WORDS:
            log_print("Ending session. Bye!")
            sys.exit(0)
        if not ans:
            log_print("Sorry I didn't catch that - could you try again?")
            continue
        if not valid:
            return ans

        if ans in YES_WORDS: ans = "yes"
        if ans in NO_WORDS: ans = "no"

        if ans in valid:
            return ans

        log_print(f"Invalid input: '{ans}'. I'm expecting one of [{', '.join(valid)}]")


def start():
    log_print('------ Wi-Fi Troubleshooting Assistant ------')
    log_print('Type exit or quit anytime to quit. Type \'restart\' to restart.')
    while True:
        ans = ask("What's the issue you're experiencing ? ('can't connect', 'slow/unstable', 'forgot password')")

        if ans == 'restart':
            continue

        if 'forgot' in ans or 'password' in ans:
            forgot_flow()
        elif 'slow' in ans or 'lag' in ans or 'speed' in ans or 'packet loss' in ans or 'unstable' in ans:
            slow_flow()
        elif 'connect' in ans or 'wifi' in ans or 'wi-fi' in ans or 'internet' in ans:
            connect_flow()
        else:
            log_print("\nI can help with unstable / spotty wifi, slow wifi, or connection issues")
            continue

        # hand off to human if the issue isn't solved by chatbot
        next_step = ask("Would you like to restart or talk to a human ? (restart/human/exit)",
                        valid={"restart", "human", "exit"}
                        )
        
        if next_step == 'restart':
            continue
        
        if next_step == 'human':
            log_print("Ok - I'll hand off with a summary of the steps we've tried here. Thanks !")
        log_print('Goodbye!')
        break

def forgot_flow():
    log_print('-- Forgot Wi-fi Password --')
    # Check if this is for a home network or other
    env = ask('Is this your home network? (yes/no)', valid={'yes', 'no'})
    # for home network
    if env == 'yes':
        log_print('You can view/reset your password in your router admin page or ISP app')
        done = ask("Were you able to reset/retreive your password? (yes/no)", valid={'yes', 'no'})
        if done == 'yes':
            log_print('All set ! Welcome back online')
            return
        else:
            log_print("No worries — I’ll hand off to a human with instructions for your router model.")
    # for other
    else:
        log_print("For workplace/others, contact the network owner or admin for credentials.")
        log_print("I can hand off to a human if you need help finding the right contact.")


def slow_flow():
    log_print('-- Slow Internet --')
    # check if its all devices or one
    which = ask('Are all devices slow, or just this one? (all/one)', valid={'all', 'one'})

    # if all devices then its likely congestion or ISP plan issues
    if which == 'all':
        peak = ask("Is it peak time (evening)? (yes/no)", valid={'yes', 'no'})
        if peak == 'yes':
            log_print("Likely due to congestion. Check if early morning or afternoon is still slow or talk to your ISP for plan options")
        else:
            log_print("Try restarting your router and then doing an internet speed test. If the speeds are much slower compared to your internet plan, contact your ISP for support")
    # if one device
    else:
        tabs = ask('Close heavy apps/processes and unused tabs. Did that improve your wifi ? (yes/no)', valid={'yes', 'no'})
        if tabs == 'yes':
            log_print('Great! Having too many tabs or processes open can consume a lot of bandwidth, try to close anything you don\'t need')
            return
        
        # hardware check
        update = ask("Check for any driver updates or OS updates. After updating, did it improve? (yes/no)", valid={'yes', 'no'})
        if update == 'yes':
            log_print('Nice! Wifi speed back to normal')
            return

        # router location respective to your device
        location = ask("Are you farther from your router compared to other, faster, devices ? (yes/no)", valid={'yes', 'no'})
        if location == 'yes':
            close = ask("Try getting closer to your router or moving your router closer to you (Or use ethernet cable). Did that improve your wifi speed ? (yes/no)", valid={'yes', 'no'})
            if close == 'yes':
                log_print('Awesome! Try to place your router in the most center location of your home in the future.')
                return
            
        # check if other devices are using too much bandwidth
        other = ask("Check if someone else is using too much bandwidth via your ISP admin panel. If you don't have access to your\
 admin panel then ask around to see if anyone is downloading something big or running heavy processes. Was there someone using a lot of bandwidth? (yes/no)", valid={'yes', 'no'}
                    )
        if other == 'yes':
            fix = ask('Use a wired connection (ethernet) or have the other person limit their bandwidth usage. Did that improve your wifi ? (yes/no)', valid={'yes', 'no'})
            if fix == 'yes':
                log_print("Nice, that fixed it !")
                return
        
        log_print('Thanks for trying these steps, I\'ll hand off to a human with a summary of the steps we\'ve tried so far')

def connect_flow():
    log_print('\n-- Connection Check --')
    # first check if wifi is turned on
    ans = ask('Is your wifi turned on for this device ? (yes/no)', valid={'yes', 'no'})
    if ans == 'no':
        ans2 = ask('Please enable Wi-fi and try reconnecting. Did it work ?', valid={'yes', 'no'})
        if ans2 == 'yes':
            log_print("Great, you're back online !")
            return
    
    # check if router lights are on
    lights = ask('Are your router lights normal ? (yes/no/not sure)', valid={'yes', 'no', 'not sure'})
    if lights in ('no', 'not sure'):
        restart = ask('Try restarting the router (unplug power and then plug back in, wait 2 mins). Did that work ? (yes/no)', valid={'yes', 'no'})
        if restart == 'yes':
            log_print('Nice! restarting fixed it!')
            return
    
    # check if its the device
    device = ask("Try 'Forget network' then rejoin. Did reconnecting work? (yes/no)", valid={'yes', 'no'})
    if device == 'yes':
        log_print('Awesome, connections restored!')
        return
    
    # Driver or OS update
    update = ask("Check for any driver updates or OS updates. After updating, did it connect? (yes/no)", valid={'yes', 'no'})
    if update == 'yes':
        log_print('Nice! Wifi connected and software up to date 😎')
        return

    # Check if other devices are offline (likely ISP)
    isp = ask("Are any other devices in your household also offline? (yes, no)", valid={'yes', 'no'})
    if isp == 'yes':
        log_print('Likely that your Internet Service Provider is having an outage. Keep your router on and service should resume automatically')
    else:
        log_print('Thanks for trying these steps, I\'ll hand off to a human with a summary of the steps we\'ve tried so far')

if __name__ == '__main__':
    # import time
    try:
        start()
    except KeyboardInterrupt:
        log_print('\nSession ended')
    finally:
        log.close()
