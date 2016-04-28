def add_anchor_segment(powerline):
    import os
    
    # User
    if powerline.args.shell == 'bash':
        user_prompt = ' \\u '
    elif powerline.args.shell == 'zsh':
        user_prompt = ' %n '
    else:
        user_prompt = ' %s ' % os.getenv('USER')

    bgcolor = Color.ANCHOR_BG

    # Host
    if powerline.args.shell == 'bash':
        host_prompt = ' \\h '
    elif powerline.args.shell == 'zsh':
        host_prompt = ' %m '
    else:
        import socket
        host_prompt = ' %s ' % socket.gethostname().split('.')[0]

    powerline.append(user_prompt + "@" + host_prompt, Color.ANCHOR_FG, bgcolor)

