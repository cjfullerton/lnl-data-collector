import glob

def read_param_name_list():

    param_name_file = open("param_names.txt")
    raw_param_name_list = param_name_file.read()
    param_name_list = raw_param_name_list.split('\n')[0:-1]

    return param_name_list


def get_data_files():

    data_files = glob.glob("*__data.csv")

    return data_files

def process_data_file(data_file_filename):

    split_filename = data_file_filename.split("_")

    expt_id = split_filename[0]
    job_id = split_filename[1]

    data_file = open(data_file_filename)
    raw_data_file = data_file.read()

    data_list =  [line.split(",",1) for line in raw_data_file.split("\n")]
    data_dict = dict(data_list[1:-1])

    return expt_id, job_id, data_dict

def get_params_from_data_dict(data_dict, param_name_list):

    param = []

    for param_name in param_name_list:
        param.append(data_dict[param_name])

    return param

def main():

    param_name_list = read_param_name_list()

    column_header_list = ['expt_id','job_id']
    column_header_list = column_header_list + param_name_list

    output = open('test_out.csv', 'w');

    for header in column_header_list:
        output.write('%s,' % header)

    output.write('\n')


    data_file_list = get_data_files()

    for data_file in data_file_list:

        expt_id_i, job_id_i, data_dict_i = process_data_file(data_file)
        params_i = get_params_from_data_dict(data_dict_i,param_name_list)
        params_out_list_i = [expt_id_i, job_id_i]
        params_out_list_i = params_out_list_i + params_i

        for param_out in params_out_list_i:
            output.write('%s,' % param_out)

        output.write("\n")

    output.close()

if __name__ == '__main__':
    main()



