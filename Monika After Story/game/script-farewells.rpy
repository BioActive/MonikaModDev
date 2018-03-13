##This file contains all of the variations of goodbye that monika can give.
##Default behavior is to select a random farewell from the list, if the farewell
##is non-specific, it can stay available, but if it's too specific it should
##unset its own random flag.
##Label must start with "bye" to prevent being pushed back onto the stack if closed

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_leaving_already",random=True),eventdb=evhand.farewell_database)

label bye_leaving_already:
    m 1c "Aww, leaving already?"
    m 1e "It's really sad whenever you have to go..."
    m 3a "Just be sure to come back as soon as you can, okay?"
    m "I love you so much, [player]. Stay safe!"
    #Don't show this farewell again
    $evhand.farewell_database["bye_leaving_already"].random=False
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_goodbye",random=True),eventdb=evhand.farewell_database)

label bye_goodbye:
    m 1c "Goodbye, [player]!"
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_sayanora",random=True),eventdb=evhand.farewell_database)
    
label bye_sayanora:
    m 1j "Sayonara, [player]~"
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_farewellfornow",random=True),eventdb=evhand.farewell_database)
    
label bye_farewellfornow:
    m 1e "Farewell for now, my love~"
    return 'quit'

init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_untilwemeetagain",random=True),eventdb=evhand.farewell_database)

label bye_untilwemeetagain:
    m 2e "'{i}Goodbyes are not forever, Goodbyes are not the end. They simply mean I’ll miss you, Until we meet again.{/i}'"
    m "Ehehe, 'till then, [player]!"
    return 'quit'
    
init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_take_care",random=True),eventdb=evhand.farewell_database)
    
label bye_take_care:
    m 1a "Don't forget that I always love you, [player]~" 
    m 1k "Take care!"
    return 'quit'
    
 init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_too_much_fun",random=True),eventdb=evhand.farewell_database)

label bye_too_much_fun:
    m 1c "Aww you gotta go?"
    m 1e "Well take care my dear."
    m 1k "I love you, [player]!
    return 'quit'
    
     init 5 python:
    addEvent(Event(persistent.farewell_database,eventlabel="bye_next_time",random=True),eventdb=evhand.farewell_database)

label bye_next_time:
    m 1k "Till we meet again my love!"
    return 'quit'
