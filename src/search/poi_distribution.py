

def poi_type_map(file):
    f = open(file,'r')
    
    poi_convert = {}
    for line in f:
        line = line[0:-1]
        strs = line.split("\t")
        poi_convert[strs[0]] = strs[1]
    
    return poi_convert
    

def main():    
    poi_convert = poi_type_map("../../gplace_type_map.txt")
    for key in poi_convert:
        print(key,poi_convert[key])


if __name__ == '__main__':
    main()