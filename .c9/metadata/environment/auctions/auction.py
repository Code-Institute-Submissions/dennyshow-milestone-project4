{"filter":false,"title":"auction.py","tooltip":"/auctions/auction.py","undoManager":{"mark":56,"position":56,"stack":[[{"start":{"row":0,"column":0},"end":{"row":17,"column":29},"action":"insert","lines":["from django.contrib.auth.models import User","from bids.models import Bid","from auctions.models import Auction","from django.utils import timezone","from datetime import datetime, timedelta","","def remaining_time(auction):","    auction = Auction.objects.filter()","    time_left = auction.end_time - timezone.now()","    no_of_days, seconds = time_left.no_days, time_left.seconds","    hour = no_of_days * 24 + seconds // 3600","    minutes = (seconds % 3600) // 60","    seconds = seconds % 60","    ","    time_left = str(\"hour\") + \"h\" + str(\"minutes\") + \"m\" + str(\"seconds\") + \"s\"","    expires = no_of_days","    ","    return time_left, expires"],"id":1}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":27},"action":"remove","lines":["from bids.models import Bid"],"id":2},{"start":{"row":0,"column":43},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":26},"action":"remove","lines":["auction"],"id":3},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["r"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["e"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["q"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["u"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["e"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["s"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":[","],"id":4}],[{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":[" "],"id":5},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["a"]},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"insert","lines":["u"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"insert","lines":["c"]},{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"insert","lines":["i"],"id":6},{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"insert","lines":["o"]},{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"insert","lines":["n"]},{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"insert","lines":["_"]},{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"insert","lines":["i"]},{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":40},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"remove","lines":["d"],"id":8},{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"remove","lines":["i"]},{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"remove","lines":["_"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":18},"action":"remove","lines":["remaining_time"],"id":9},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["t"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["i"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["m"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["e"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["_"]}],[{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["f"],"id":10},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["o"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["r"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["_"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["b"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["i"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["d"],"id":11},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["i"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["n"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["g"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":20},"action":"remove","lines":["time_for_bidding"],"id":12},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["t"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["o"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["_"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["a"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["u"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["c"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["i"],"id":13},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["o"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["n"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["_"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["a"]}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["_"],"id":14},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["b"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["i"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"remove","lines":["d"],"id":15},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"remove","lines":["i"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"remove","lines":["b"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"remove","lines":["_"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"remove","lines":["a"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"remove","lines":["_"]}],[{"start":{"row":7,"column":38},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["t"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["i"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["m"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["_"],"id":17},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["l"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["e"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["f"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":[" "],"id":18},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":[" "],"id":19},{"start":{"row":8,"column":16},"end":{"row":9,"column":0},"action":"insert","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":10},"end":{"row":10,"column":4},"action":"remove","lines":["eft = ","    ","    "],"id":22},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["l"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["_"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["e"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["m"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":["i"]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"remove","lines":["t"]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":9,"column":49},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":24},{"start":{"row":9,"column":49},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":13},"action":"remove","lines":["left"],"id":25},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["r"]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["e"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":["m"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["a"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["i"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["n"]}],[{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["i"],"id":26},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["n"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["g"]}],[{"start":{"row":10,"column":34},"end":{"row":10,"column":35},"action":"remove","lines":["t"],"id":27},{"start":{"row":10,"column":33},"end":{"row":10,"column":34},"action":"remove","lines":["f"]},{"start":{"row":10,"column":32},"end":{"row":10,"column":33},"action":"remove","lines":["e"]},{"start":{"row":10,"column":31},"end":{"row":10,"column":32},"action":"remove","lines":["l"]}],[{"start":{"row":10,"column":31},"end":{"row":10,"column":32},"action":"insert","lines":["r"],"id":28},{"start":{"row":10,"column":32},"end":{"row":10,"column":33},"action":"insert","lines":["e"]},{"start":{"row":10,"column":33},"end":{"row":10,"column":34},"action":"insert","lines":["m"]},{"start":{"row":10,"column":34},"end":{"row":10,"column":35},"action":"insert","lines":["a"]},{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"remove","lines":["n"],"id":29}],[{"start":{"row":10,"column":35},"end":{"row":10,"column":36},"action":"insert","lines":["i"],"id":30},{"start":{"row":10,"column":36},"end":{"row":10,"column":37},"action":"insert","lines":["n"]},{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"insert","lines":["i"]},{"start":{"row":10,"column":38},"end":{"row":10,"column":39},"action":"insert","lines":["n"]},{"start":{"row":10,"column":39},"end":{"row":10,"column":40},"action":"insert","lines":["g"]}],[{"start":{"row":10,"column":26},"end":{"row":10,"column":40},"action":"remove","lines":["time_remaining"],"id":31},{"start":{"row":10,"column":26},"end":{"row":10,"column":27},"action":"insert","lines":["t"]},{"start":{"row":10,"column":27},"end":{"row":10,"column":28},"action":"insert","lines":["i"]},{"start":{"row":10,"column":28},"end":{"row":10,"column":29},"action":"insert","lines":["m"]}],[{"start":{"row":10,"column":26},"end":{"row":10,"column":29},"action":"remove","lines":["tim"],"id":32},{"start":{"row":10,"column":26},"end":{"row":10,"column":40},"action":"insert","lines":["time_remaining"]}],[{"start":{"row":10,"column":50},"end":{"row":10,"column":59},"action":"remove","lines":["time_left"],"id":33},{"start":{"row":10,"column":50},"end":{"row":10,"column":51},"action":"insert","lines":["t"]},{"start":{"row":10,"column":51},"end":{"row":10,"column":52},"action":"insert","lines":["i"]},{"start":{"row":10,"column":52},"end":{"row":10,"column":53},"action":"insert","lines":["m"]},{"start":{"row":10,"column":53},"end":{"row":10,"column":54},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":53},"end":{"row":10,"column":54},"action":"remove","lines":["e"],"id":34},{"start":{"row":10,"column":52},"end":{"row":10,"column":53},"action":"remove","lines":["m"]},{"start":{"row":10,"column":51},"end":{"row":10,"column":52},"action":"remove","lines":["i"]},{"start":{"row":10,"column":50},"end":{"row":10,"column":51},"action":"remove","lines":["t"]}],[{"start":{"row":10,"column":50},"end":{"row":10,"column":51},"action":"insert","lines":["t"],"id":35},{"start":{"row":10,"column":51},"end":{"row":10,"column":52},"action":"insert","lines":["i"]},{"start":{"row":10,"column":52},"end":{"row":10,"column":53},"action":"insert","lines":["m"]},{"start":{"row":10,"column":53},"end":{"row":10,"column":54},"action":"insert","lines":["e"]},{"start":{"row":10,"column":54},"end":{"row":10,"column":55},"action":"insert","lines":["_"]}],[{"start":{"row":10,"column":55},"end":{"row":10,"column":56},"action":"insert","lines":["r"],"id":36},{"start":{"row":10,"column":56},"end":{"row":10,"column":57},"action":"insert","lines":["e"]},{"start":{"row":10,"column":57},"end":{"row":10,"column":58},"action":"insert","lines":["m"]},{"start":{"row":10,"column":58},"end":{"row":10,"column":59},"action":"insert","lines":["a"]},{"start":{"row":10,"column":59},"end":{"row":10,"column":60},"action":"insert","lines":["i"]},{"start":{"row":10,"column":60},"end":{"row":10,"column":61},"action":"insert","lines":["n"]},{"start":{"row":10,"column":61},"end":{"row":10,"column":62},"action":"insert","lines":["i"]},{"start":{"row":10,"column":62},"end":{"row":10,"column":63},"action":"insert","lines":["n"]}],[{"start":{"row":10,"column":63},"end":{"row":10,"column":64},"action":"insert","lines":["g"],"id":37}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":44},"action":"remove","lines":["hour = no_of_days * 24 + seconds // 3600"],"id":38},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "]},{"start":{"row":10,"column":72},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":14,"column":17},"end":{"row":14,"column":33},"action":"remove","lines":["tr(\"hour\") + \"h\""],"id":39}],[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":[" "],"id":40},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"remove","lines":["+"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"remove","lines":[" "]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"remove","lines":["s"]}],[{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"remove","lines":["s"],"id":41},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"remove","lines":["e"]}],[{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["y"],"id":42}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":10},"action":"remove","lines":["expiry"],"id":43},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["d"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["a"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["y"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["s"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["_"]},{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["l"]},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["f"],"id":44},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":22},"end":{"row":17,"column":29},"action":"remove","lines":["expires"],"id":45},{"start":{"row":17,"column":22},"end":{"row":17,"column":23},"action":"insert","lines":["d"]},{"start":{"row":17,"column":23},"end":{"row":17,"column":24},"action":"insert","lines":["a"]},{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["y"]},{"start":{"row":17,"column":25},"end":{"row":17,"column":26},"action":"insert","lines":["s"]},{"start":{"row":17,"column":26},"end":{"row":17,"column":27},"action":"insert","lines":["_"]},{"start":{"row":17,"column":27},"end":{"row":17,"column":28},"action":"insert","lines":["l"]},{"start":{"row":17,"column":28},"end":{"row":17,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":["f"],"id":46},{"start":{"row":17,"column":30},"end":{"row":17,"column":31},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":33},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":47},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["r"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["i"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"remove","lines":["n"],"id":48},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"remove","lines":["i"]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":["r"]}],[{"start":{"row":17,"column":4},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":59},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["p"],"id":60},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["r"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["i"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["n"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":9},"end":{"row":17,"column":11},"action":"insert","lines":["()"],"id":61}],[{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["a"],"id":62},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["u"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["c"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["t"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["i"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["o"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["n"]}],[{"start":{"row":17,"column":10},"end":{"row":17,"column":17},"action":"remove","lines":["auction"],"id":63},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"insert","lines":["t"]},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"insert","lines":["i"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"insert","lines":["m"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"insert","lines":["e"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"insert","lines":["_"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"insert","lines":["l"]}],[{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"insert","lines":["e"],"id":64},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"insert","lines":["f"]},{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":4},"end":{"row":17,"column":20},"action":"remove","lines":["print(time_left)"],"id":65}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["p"],"id":66},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["r"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["i"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["n"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":9},"end":{"row":6,"column":11},"action":"insert","lines":["()"],"id":67}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["t"],"id":68},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["o"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["_"]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["a"],"id":69},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["u"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["c"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["t"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["i"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["o"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["n"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":19,"column":31},"end":{"row":19,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1577996706290,"hash":"4b95fcb64f61001735785a5b2cc132135789b025"}