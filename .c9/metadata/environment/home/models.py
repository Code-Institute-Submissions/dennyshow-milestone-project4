{"changed":true,"filter":false,"title":"models.py","tooltip":"/home/models.py","value":"from django.db import models\nfrom products.models import Product\n\n# Create your models here.\n\nclass Page(models.Model):\n    product_id = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)\n    \n    def __str__(self):\n        return \"product_id:\" + str(self.product_id)","undoManager":{"mark":76,"position":76,"stack":[[{"start":{"row":6,"column":25},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["p"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["r"]},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["o"]},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["d"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["u"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["c"]},{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["_"],"id":14},{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["i"]},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["d"]}],[{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":[" "],"id":15},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":[" "],"id":16},{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":["m"]},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["o"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["d"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["e"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["l"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["."],"id":17},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["F"]}],[{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"remove","lines":["F"],"id":18},{"start":{"row":7,"column":24},"end":{"row":7,"column":34},"action":"insert","lines":["ForeignKey"]}],[{"start":{"row":7,"column":34},"end":{"row":7,"column":36},"action":"insert","lines":["()"],"id":19}],[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["P"],"id":20},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["r"]},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["o"]},{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["d"]},{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["u"]},{"start":{"row":7,"column":40},"end":{"row":7,"column":41},"action":"insert","lines":["c"]},{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"insert","lines":[","],"id":21}],[{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"insert","lines":[" "],"id":22}],[{"start":{"row":7,"column":44},"end":{"row":7,"column":45},"action":"insert","lines":["o"],"id":23},{"start":{"row":7,"column":45},"end":{"row":7,"column":46},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":44},"end":{"row":7,"column":46},"action":"remove","lines":["on"],"id":24},{"start":{"row":7,"column":44},"end":{"row":7,"column":53},"action":"insert","lines":["on_delete"]}],[{"start":{"row":7,"column":53},"end":{"row":7,"column":54},"action":"insert","lines":["="],"id":25},{"start":{"row":7,"column":54},"end":{"row":7,"column":55},"action":"insert","lines":["m"]},{"start":{"row":7,"column":55},"end":{"row":7,"column":56},"action":"insert","lines":["o"]},{"start":{"row":7,"column":56},"end":{"row":7,"column":57},"action":"insert","lines":["d"]},{"start":{"row":7,"column":57},"end":{"row":7,"column":58},"action":"insert","lines":["e"]},{"start":{"row":7,"column":58},"end":{"row":7,"column":59},"action":"insert","lines":["l"]},{"start":{"row":7,"column":59},"end":{"row":7,"column":60},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":60},"end":{"row":7,"column":61},"action":"insert","lines":["."],"id":26},{"start":{"row":7,"column":61},"end":{"row":7,"column":62},"action":"insert","lines":["C"]},{"start":{"row":7,"column":62},"end":{"row":7,"column":63},"action":"insert","lines":["A"]},{"start":{"row":7,"column":63},"end":{"row":7,"column":64},"action":"insert","lines":["S"]}],[{"start":{"row":7,"column":61},"end":{"row":7,"column":64},"action":"remove","lines":["CAS"],"id":27},{"start":{"row":7,"column":61},"end":{"row":7,"column":68},"action":"insert","lines":["CASCADE"]}],[{"start":{"row":2,"column":27},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"]},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":29},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["p"]}],[{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["r"],"id":30},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["o"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["d"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["u"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["c"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["t"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["s"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["."]}],[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["m"],"id":31},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["o"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["d"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["e"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["l"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":[" "],"id":32},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["i"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["m"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["p"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["r"],"id":33},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":[" "],"id":34},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["P"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["r"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["o"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["d"]}],[{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["u"],"id":35},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["c"]},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":[" "],"id":36}],[{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"remove","lines":[" "],"id":37}],[{"start":{"row":10,"column":3},"end":{"row":10,"column":61},"action":"remove","lines":[" bid_id = models.ForeignKey(Bid, on_delete=models.CASCADE)"],"id":83},{"start":{"row":10,"column":2},"end":{"row":10,"column":3},"action":"remove","lines":[" "]},{"start":{"row":10,"column":1},"end":{"row":10,"column":2},"action":"remove","lines":[" "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":1},"action":"remove","lines":[" "]},{"start":{"row":9,"column":63},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":27},"action":"remove","lines":["from bids.models import Bid"],"id":84},{"start":{"row":1,"column":43},"end":{"row":2,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":71},"end":{"row":12,"column":72},"action":"remove","lines":["d"],"id":85},{"start":{"row":12,"column":70},"end":{"row":12,"column":71},"action":"remove","lines":["i"]},{"start":{"row":12,"column":69},"end":{"row":12,"column":70},"action":"remove","lines":["b"]}],[{"start":{"row":12,"column":69},"end":{"row":12,"column":70},"action":"insert","lines":["p"],"id":86},{"start":{"row":12,"column":70},"end":{"row":12,"column":71},"action":"insert","lines":["r"]},{"start":{"row":12,"column":71},"end":{"row":12,"column":72},"action":"insert","lines":["o"]}],[{"start":{"row":12,"column":69},"end":{"row":12,"column":75},"action":"remove","lines":["pro_id"],"id":87},{"start":{"row":12,"column":69},"end":{"row":12,"column":79},"action":"insert","lines":["product_id"]}],[{"start":{"row":12,"column":54},"end":{"row":12,"column":55},"action":"remove","lines":["d"],"id":88},{"start":{"row":12,"column":53},"end":{"row":12,"column":54},"action":"remove","lines":["i"]},{"start":{"row":12,"column":52},"end":{"row":12,"column":53},"action":"remove","lines":["_"]},{"start":{"row":12,"column":51},"end":{"row":12,"column":52},"action":"remove","lines":["d"]},{"start":{"row":12,"column":50},"end":{"row":12,"column":51},"action":"remove","lines":["i"]},{"start":{"row":12,"column":49},"end":{"row":12,"column":50},"action":"remove","lines":["b"]}],[{"start":{"row":12,"column":49},"end":{"row":12,"column":50},"action":"insert","lines":["p"],"id":89},{"start":{"row":12,"column":50},"end":{"row":12,"column":51},"action":"insert","lines":["r"]},{"start":{"row":12,"column":51},"end":{"row":12,"column":52},"action":"insert","lines":["o"]}],[{"start":{"row":12,"column":49},"end":{"row":12,"column":52},"action":"remove","lines":["pro"],"id":90},{"start":{"row":12,"column":49},"end":{"row":12,"column":59},"action":"insert","lines":["product_id"]}],[{"start":{"row":7,"column":68},"end":{"row":7,"column":69},"action":"insert","lines":[","],"id":91}],[{"start":{"row":7,"column":69},"end":{"row":7,"column":70},"action":"insert","lines":[" "],"id":92}],[{"start":{"row":7,"column":70},"end":{"row":7,"column":71},"action":"insert","lines":["d"],"id":93},{"start":{"row":7,"column":71},"end":{"row":7,"column":72},"action":"insert","lines":["e"]},{"start":{"row":7,"column":72},"end":{"row":7,"column":73},"action":"insert","lines":["f"]}],[{"start":{"row":7,"column":70},"end":{"row":7,"column":73},"action":"remove","lines":["def"],"id":94},{"start":{"row":7,"column":70},"end":{"row":7,"column":77},"action":"insert","lines":["default"]}],[{"start":{"row":7,"column":77},"end":{"row":7,"column":78},"action":"insert","lines":["="],"id":95}],[{"start":{"row":7,"column":78},"end":{"row":7,"column":80},"action":"insert","lines":["''"],"id":96}],[{"start":{"row":8,"column":62},"end":{"row":8,"column":63},"action":"insert","lines":[","],"id":97}],[{"start":{"row":8,"column":63},"end":{"row":8,"column":64},"action":"insert","lines":[" "],"id":98},{"start":{"row":8,"column":64},"end":{"row":8,"column":65},"action":"insert","lines":["d"]},{"start":{"row":8,"column":65},"end":{"row":8,"column":66},"action":"insert","lines":["e"]}],[{"start":{"row":8,"column":64},"end":{"row":8,"column":66},"action":"remove","lines":["de"],"id":99},{"start":{"row":8,"column":64},"end":{"row":8,"column":71},"action":"insert","lines":["default"]}],[{"start":{"row":8,"column":71},"end":{"row":8,"column":72},"action":"insert","lines":["="],"id":100}],[{"start":{"row":8,"column":72},"end":{"row":8,"column":74},"action":"insert","lines":["''"],"id":101}],[{"start":{"row":7,"column":80},"end":{"row":7,"column":81},"action":"insert","lines":[","],"id":102}],[{"start":{"row":7,"column":81},"end":{"row":7,"column":82},"action":"insert","lines":[" "],"id":103},{"start":{"row":7,"column":82},"end":{"row":7,"column":83},"action":"insert","lines":["e"]},{"start":{"row":7,"column":83},"end":{"row":7,"column":84},"action":"insert","lines":["d"]},{"start":{"row":7,"column":84},"end":{"row":7,"column":85},"action":"insert","lines":["i"]},{"start":{"row":7,"column":85},"end":{"row":7,"column":86},"action":"insert","lines":["t"]},{"start":{"row":7,"column":86},"end":{"row":7,"column":87},"action":"insert","lines":["a"]}],[{"start":{"row":7,"column":87},"end":{"row":7,"column":88},"action":"insert","lines":["b"],"id":104},{"start":{"row":7,"column":88},"end":{"row":7,"column":89},"action":"insert","lines":["l"]},{"start":{"row":7,"column":89},"end":{"row":7,"column":90},"action":"insert","lines":["e"]},{"start":{"row":7,"column":90},"end":{"row":7,"column":91},"action":"insert","lines":["="]},{"start":{"row":7,"column":91},"end":{"row":7,"column":92},"action":"insert","lines":["F"]}],[{"start":{"row":7,"column":92},"end":{"row":7,"column":93},"action":"insert","lines":["a"],"id":105},{"start":{"row":7,"column":93},"end":{"row":7,"column":94},"action":"insert","lines":["l"]},{"start":{"row":7,"column":94},"end":{"row":7,"column":95},"action":"insert","lines":["s"]},{"start":{"row":7,"column":95},"end":{"row":7,"column":96},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":96},"end":{"row":7,"column":97},"action":"insert","lines":[","],"id":106}],[{"start":{"row":7,"column":97},"end":{"row":7,"column":98},"action":"insert","lines":[" "],"id":107},{"start":{"row":7,"column":98},"end":{"row":7,"column":99},"action":"insert","lines":["n"]},{"start":{"row":7,"column":99},"end":{"row":7,"column":100},"action":"insert","lines":["u"]},{"start":{"row":7,"column":100},"end":{"row":7,"column":101},"action":"insert","lines":["l"]}],[{"start":{"row":7,"column":101},"end":{"row":7,"column":102},"action":"insert","lines":["l"],"id":108}],[{"start":{"row":7,"column":102},"end":{"row":7,"column":103},"action":"insert","lines":["="],"id":109},{"start":{"row":7,"column":103},"end":{"row":7,"column":104},"action":"insert","lines":["T"]},{"start":{"row":7,"column":104},"end":{"row":7,"column":105},"action":"insert","lines":["r"]},{"start":{"row":7,"column":105},"end":{"row":7,"column":106},"action":"insert","lines":["y"]}],[{"start":{"row":7,"column":106},"end":{"row":7,"column":107},"action":"insert","lines":["e"],"id":110}],[{"start":{"row":7,"column":106},"end":{"row":7,"column":107},"action":"remove","lines":["e"],"id":111},{"start":{"row":7,"column":105},"end":{"row":7,"column":106},"action":"remove","lines":["y"]}],[{"start":{"row":7,"column":105},"end":{"row":7,"column":106},"action":"insert","lines":["u"],"id":112},{"start":{"row":7,"column":106},"end":{"row":7,"column":107},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":103},"end":{"row":7,"column":107},"action":"remove","lines":["True"],"id":113},{"start":{"row":7,"column":102},"end":{"row":7,"column":103},"action":"remove","lines":["="]},{"start":{"row":7,"column":101},"end":{"row":7,"column":102},"action":"remove","lines":["l"]},{"start":{"row":7,"column":100},"end":{"row":7,"column":101},"action":"remove","lines":["l"]},{"start":{"row":7,"column":99},"end":{"row":7,"column":100},"action":"remove","lines":["u"]},{"start":{"row":7,"column":98},"end":{"row":7,"column":99},"action":"remove","lines":["n"]}],[{"start":{"row":7,"column":98},"end":{"row":7,"column":99},"action":"insert","lines":["b"],"id":114},{"start":{"row":7,"column":99},"end":{"row":7,"column":100},"action":"insert","lines":["l"]}],[{"start":{"row":7,"column":99},"end":{"row":7,"column":100},"action":"remove","lines":["l"],"id":115},{"start":{"row":7,"column":98},"end":{"row":7,"column":99},"action":"remove","lines":["b"]}],[{"start":{"row":7,"column":98},"end":{"row":7,"column":99},"action":"insert","lines":["n"],"id":116},{"start":{"row":7,"column":99},"end":{"row":7,"column":100},"action":"insert","lines":["u"]},{"start":{"row":7,"column":100},"end":{"row":7,"column":101},"action":"insert","lines":["l"]},{"start":{"row":7,"column":101},"end":{"row":7,"column":102},"action":"insert","lines":["l"]},{"start":{"row":7,"column":102},"end":{"row":7,"column":103},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":103},"end":{"row":7,"column":105},"action":"insert","lines":["''"],"id":117}],[{"start":{"row":7,"column":103},"end":{"row":7,"column":105},"action":"remove","lines":["''"],"id":118}],[{"start":{"row":7,"column":103},"end":{"row":7,"column":104},"action":"insert","lines":["F"],"id":119},{"start":{"row":7,"column":104},"end":{"row":7,"column":105},"action":"insert","lines":["a"]},{"start":{"row":7,"column":105},"end":{"row":7,"column":106},"action":"insert","lines":["l"]},{"start":{"row":7,"column":106},"end":{"row":7,"column":107},"action":"insert","lines":["s"]},{"start":{"row":7,"column":107},"end":{"row":7,"column":108},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":70},"end":{"row":7,"column":80},"action":"remove","lines":["default=''"],"id":120},{"start":{"row":7,"column":69},"end":{"row":7,"column":70},"action":"remove","lines":[" "]},{"start":{"row":7,"column":68},"end":{"row":7,"column":69},"action":"remove","lines":[","]}],[{"start":{"row":7,"column":86},"end":{"row":7,"column":96},"action":"remove","lines":["null=False"],"id":121},{"start":{"row":7,"column":85},"end":{"row":7,"column":86},"action":"remove","lines":[" "]},{"start":{"row":7,"column":84},"end":{"row":7,"column":85},"action":"remove","lines":[","]},{"start":{"row":7,"column":83},"end":{"row":7,"column":84},"action":"remove","lines":["e"]},{"start":{"row":7,"column":82},"end":{"row":7,"column":83},"action":"remove","lines":["s"]},{"start":{"row":7,"column":81},"end":{"row":7,"column":82},"action":"remove","lines":["l"]},{"start":{"row":7,"column":80},"end":{"row":7,"column":81},"action":"remove","lines":["a"]},{"start":{"row":7,"column":79},"end":{"row":7,"column":80},"action":"remove","lines":["F"]},{"start":{"row":7,"column":78},"end":{"row":7,"column":79},"action":"remove","lines":["="]},{"start":{"row":7,"column":77},"end":{"row":7,"column":78},"action":"remove","lines":["e"]},{"start":{"row":7,"column":76},"end":{"row":7,"column":77},"action":"remove","lines":["l"]},{"start":{"row":7,"column":75},"end":{"row":7,"column":76},"action":"remove","lines":["b"]},{"start":{"row":7,"column":74},"end":{"row":7,"column":75},"action":"remove","lines":["a"]}],[{"start":{"row":7,"column":73},"end":{"row":7,"column":74},"action":"remove","lines":["t"],"id":122},{"start":{"row":7,"column":72},"end":{"row":7,"column":73},"action":"remove","lines":["i"]},{"start":{"row":7,"column":71},"end":{"row":7,"column":72},"action":"remove","lines":["d"]},{"start":{"row":7,"column":70},"end":{"row":7,"column":71},"action":"remove","lines":["e"]},{"start":{"row":7,"column":69},"end":{"row":7,"column":70},"action":"remove","lines":[" "]},{"start":{"row":7,"column":68},"end":{"row":7,"column":69},"action":"remove","lines":[","]}],[{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"insert","lines":[" "],"id":123},{"start":{"row":7,"column":44},"end":{"row":7,"column":45},"action":"insert","lines":["n"]},{"start":{"row":7,"column":45},"end":{"row":7,"column":46},"action":"insert","lines":["u"]},{"start":{"row":7,"column":46},"end":{"row":7,"column":47},"action":"insert","lines":["l"]}],[{"start":{"row":7,"column":47},"end":{"row":7,"column":48},"action":"insert","lines":["l"],"id":124},{"start":{"row":7,"column":48},"end":{"row":7,"column":49},"action":"insert","lines":["="]},{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":["T"]},{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"insert","lines":["r"]},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"insert","lines":["u"]}],[{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"insert","lines":["e"],"id":125},{"start":{"row":7,"column":53},"end":{"row":7,"column":54},"action":"insert","lines":[","]}],[{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"remove","lines":["e"],"id":126},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"remove","lines":["u"]},{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"remove","lines":["r"]},{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"remove","lines":["T"]}],[{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":["F"],"id":127},{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"insert","lines":["a"]},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"insert","lines":["l"]},{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"insert","lines":["s"]},{"start":{"row":7,"column":53},"end":{"row":7,"column":54},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":49},"end":{"row":7,"column":54},"action":"remove","lines":["False"],"id":128},{"start":{"row":7,"column":49},"end":{"row":7,"column":50},"action":"insert","lines":["T"]},{"start":{"row":7,"column":50},"end":{"row":7,"column":51},"action":"insert","lines":["r"]},{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"insert","lines":["u"]},{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":43},"action":"remove","lines":["from django.contrib.auth.models import User"],"id":129},{"start":{"row":0,"column":28},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":3},"end":{"row":7,"column":75},"action":"remove","lines":[" user_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')"],"id":130},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"remove","lines":[" "]},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"remove","lines":[" "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"remove","lines":[" "]},{"start":{"row":6,"column":80},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":47},"action":"remove","lines":["user_id:\" + str(self.user_id) +"],"id":131}],[{"start":{"row":10,"column":16},"end":{"row":10,"column":17},"action":"remove","lines":[" "],"id":132},{"start":{"row":10,"column":15},"end":{"row":10,"column":17},"action":"remove","lines":["\"\""]}],[{"start":{"row":10,"column":15},"end":{"row":10,"column":16},"action":"insert","lines":["\""],"id":133}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":49},"action":"remove","lines":["image = models.ImageField(upload_to=\"images\")"],"id":134},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "]},{"start":{"row":6,"column":80},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":[" "],"id":136},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"remove","lines":["\""]}],[{"start":{"row":9,"column":16},"end":{"row":9,"column":30},"action":"remove","lines":["product_id:\" +"],"id":136}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":51},"end":{"row":9,"column":51},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"start","mode":"ace/mode/python"}},"timestamp":1578345787465}