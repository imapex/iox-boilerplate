# Gracefully handle SIGTERM and SIGINT
def handle_signal(signum, stack):
    # Raise a KeyboardInterrupt so that the main loop catches this and shuts down
    raise KeyboardInterrupt

