from selenium import webdriver
import json

def get_data(link):
    """
    Returns a list of player ids and a list of events from the match in json
    """
    driver = webdriver.Chrome(executable_path='/Users/jonathanziman/Desktop/SoccerAnalysis/socplot-master/socplot/chromedriver')
    driver.minimize_window()
    driver.get(link)
    html = driver.page_source
    driver.close()

    start_index = html.index("\"playerIdNameDictionary\":") + len("\"playerIdNameDictionary\":")
    id_data = html[start_index:]
    end_index = id_data.index(",\"periodMinuteLimits\":{")
    ids = id_data[:end_index]
    json_ids = json.loads(ids)

    start_index = html.index("\"events\":") + len("\"events\":")
    event_data = html[start_index:]
    end_index = event_data.index(",\"timeoutInSeconds\":0},")
    events = event_data[:end_index]
    json_events = json.loads(events)

    return json_ids, json_events