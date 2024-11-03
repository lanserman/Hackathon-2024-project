import json

input_file = 'pestdata.txt' 
output_file = 'pest_data.json' 

pest_data = []

with open(input_file, 'r') as file:
   
    lines = file.readlines()
    

    lines = [line.strip() for line in lines if line.strip()]  

    
    for i in range(0, len(lines), 5):
        if i + 5 <= len(lines):  
            pest = lines[i]  
            life_stage = lines[i + 1]  
            gdd_range = lines[i + 2]  
            degree_day_maps = lines[i + 3]  
            reference = lines[i + 4]  

            
            min_gdd = None
            max_gdd = None

            
            if '-' in gdd_range:
                try:
                    min_gdd, max_gdd = map(int, gdd_range.split('-'))
                except ValueError:
                    print(f"Error parsing GDD range '{gdd_range}' for pest '{pest}'. Skipping entry.")
                    continue
            else:
                
                try:
                    min_gdd = max_gdd = int(gdd_range)
                except ValueError:
                    print(f"Error parsing single GDD value '{gdd_range}' for pest '{pest}'. Skipping entry.")
                    continue

            
            try:
                degree_day_maps = list(map(int, filter(lambda x: x.isdigit(), degree_day_maps.split(', '))))
            except ValueError:
                print(f"Error parsing degree day maps '{degree_day_maps}' for pest '{pest}'. Skipping entry.")
                continue

            
            pest_data.append({
                "pest": pest,
                "life_stage": life_stage,
                "gdd_range": {
                    "min_gdd": min_gdd,
                    "max_gdd": max_gdd
                },
                "degree_day_maps": degree_day_maps,
                "reference": reference
            })

with open(output_file, 'w') as json_file:
    json.dump(pest_data, json_file, indent=4)

print(f"Data has been successfully saved to {output_file}")

