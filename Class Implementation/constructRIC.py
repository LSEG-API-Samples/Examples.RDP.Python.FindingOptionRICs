import refinitiv.dataplatform as rdp
from defClass.constructFunction import Option_RIC

app_key = open("app_key.txt", "r").read()
rdp.open_desktop_session(app_key)

ric = Option_RIC('US78378X1072', '2022-02-18', 5000, 'C')
print(ric.constructRIC())
