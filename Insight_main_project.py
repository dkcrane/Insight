## Insight Data Engineering Proejct ##
import time



def print_first_num_lines(file_name: str, num: int) -> None:
    # This program prints out the first "num" lines of "file_name."
    # This is used for testing purposes.
    file=open(file_name,'r+')
    counter=0
    for line in file:
        if counter>num:
            break
        else:
            print(line)
            counter+=1


def write_dict(file_name: str) -> dict:
    # This program reads in a file  containing the product information and outputs a dictionary
    # of the form out_dict[product_id] = department_id
    file=open(file_name,'r+')
    out_dict={}
    first_line=True
    for line in file:
        if first_line: # This block of code skips over the first line which contains the headers of the tables.
            first_line=False
        else:
            product_info = line.split(',')
            out_dict[int(product_info[0])]=int(product_info[-1]) # We require our keys/values to be integers.
    return out_dict
        
        

# Main function  
def insight_coding_challenge(order_file_name: str, product_file_name: str, out_file_name: str) -> None:
    # This program takes in the files containing (1) the product info and (2) the order info.

    # First we create the dictionary prod_dept_dict[product_id]=department_id
    t = time.time()
    prod_dept_dict = write_dict(product_file_name)

    # Time check
    print("First step completed in ",time.time()-t," seconds.")
    t = time.time()

    # Here, we loop through our order file and construct a dictionary of the form
    #  department_info_dict[department_id] = [num_orders,num_first_time_orders]
    order_file= open(order_file_name,'r+')
    department_info_dict = {}
    first_line=True
    for line in order_file:
        if first_line: # We skip over the headers in the file.
            first_line=False
        else:
            order_info=line.split(',')
            dep_num=prod_dept_dict[int(order_info[1])]
            first_time=1-int(order_info[-1])
            if dep_num not in department_info_dict:
                department_info_dict[dep_num]=[1,first_time]
            else:
                department_info_dict[dep_num][0]+=1
                department_info_dict[dep_num][1]+=first_time
    # Time check
    print("Second step completed in ",time.time()-t," seconds.")
    
    t = time.time()
    # Finally, we write the information in department_info_dict to a file.
    # We be sure and include the percentage of first_time_orders in our file.

    out_file = open(out_file_name,"w+")
    # Insert headers here.
    out_file.write('department_id,number_of_orders,number_of_first_orders,percentage')
    out_file.write('\n') 

    for key in sorted(department_info_dict): # loop through the sorted keys so the departments  are in ascending order.
        # We need the department_id, the number of orders, the number of first time orders, and the percentage
        # as strings.
        str_dep_num=str(key)+','
        str_order_num=str(department_info_dict[key][0])+','
        str_first_order_num=str(department_info_dict[key][1])+','
        str_percentage=str(round(department_info_dict[key][1]/department_info_dict[key][0],2))

        #Here, we write the data as a line in our output file.                
        out_file.write(str_dep_num+str_order_num+str_first_order_num+str_percentage)
        out_file.write("\n")

    # Time check
    print("Third step completed in ",time.time()-t," seconds.")


    

    
            
            
    
    

if __name__ == "__main__":

    
    input_order_file = "order_products__prior.csv" # file containing order information

    #input_order_file = "order_products__train.csv"  <---Could also use this file for input file.
    
    product_file = "products.csv" # file containing product information
    
    output_file = "report.csv"  # file that will contain the required output
    

    insight_coding_challenge(input_order_file, product_file, output_file)

    
    # Below we print out our report.csv file to check our work.
    print_first_num_lines(output_file,21) 

