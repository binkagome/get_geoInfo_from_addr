def main():
#    file_read()
    
    addr_latlng_1 = get_lat_lon_from_address(addr_list_1)
    addr_latlng_2 = get_lat_lon_from_address(addr_list_2)
    with open('output.csv', 'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["1", "2", "distance"])
        
        for addr0 in addr_latlng_1.keys():
            for addr1 in addr_latlng_2.keys():
                pos0 = tuple(np.array(addr_latlng_1[addr0], dtype=float))
                pos1 = tuple(np.array(addr_latlng_2[addr1], dtype=float))
                
                row = [addr0,  addr1, dist_on_sphere(pos0, pos1)]
                writer.writerow(row)
#                print(addr0, "\t", addr1,"\t")
#                print(dist_on_sphere(pos0, pos1))
