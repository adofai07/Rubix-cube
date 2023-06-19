from type_old import Cube

a = Cube([
    "   111",
    "   111",
    "   111",
    "222333444555",
    "222333444555",
    "222333444555",
    "   666",
    "   666",
    "   666"
])
a.move_list("R U R' F' R U R' U' R' F R2 U' R'".split(" "))
