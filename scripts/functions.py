def player_pass_data(events, player_id):
    """
    Returns all attempted passes for a specified player
    """
    passes = []
    for event in events:
        if event['type']['displayName'] == 'Pass':
            if event['playerId'] == int(player_id):
                    passes.append(event)
    return passes


def player_carry_data(events, player_id):
    """
    Returns all attempted passes for a specified player
    """
    carries = []
    for event in events:
        if 'carry' in event and event['player']['name'] == player:
            carries.append(event)
    return carries


def add_completed_passes(pitch, passes):
    """
    Adds completed passes to the pitch
    """
    for pass_data in passes:
        if pass_data['outcomeType']['displayName'] == 'Successful':
            pitch.plot_pass([1.2*pass_data['x'], 0.8*pass_data['y']], [1.2*pass_data['endX'], 0.8*pass_data['endY']])


def add_incompleted_passes(pitch, passes):
    """
    Adds incompleted passes to the pitch
    """
    for pass_data in passes:
        if pass_data['outcomeType']['displayName'] == 'Unsuccessful':
            pitch.plot_pass([1.2*pass_data['x'], 0.8*pass_data['y']], [1.2*pass_data['endX'], 0.8*pass_data['endY']])


def add_carries(pitch, carries):
    for carry_data in carries:
        pitch.plot_pass([carry_data['location'][0], carry_data['location'][1]], [carry_data['carry']['end_location'][0], carry_data['carry']['end_location'][1]])


def add_heatmap(pitch, x_array, y_array):
    pitch.heat_map(x_array, y_array, color='tan')
