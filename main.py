def main():
#    file_read()
    
    addr_latlng_domino = get_lat_lon_from_address(addr_list_domino)
    addr_latlng_pizzahut = get_lat_lon_from_address(addr_list_pizzahut)
    with open('output.csv', 'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Domino", "Pizzahut", "distance"])
        
        for addr0 in addr_latlng_domino.keys():
            for addr1 in addr_latlng_pizzahut.keys():
                pos0 = tuple(np.array(addr_latlng_domino[addr0], dtype=float))
                pos1 = tuple(np.array(addr_latlng_pizzahut[addr1], dtype=float))
                
                row = [addr0,  addr1, dist_on_sphere(pos0, pos1)]
                writer.writerow(row)
#                print(addr0, "\t", addr1,"\t")
#                print(dist_on_sphere(pos0, pos1))
