def list_to_dict(inp_list):
    inp_list_len=len(inp_list)
    result_dict={}
    for i in range(inp_list_len):
        if inp_list[i] in dict_mag:
            result_dict[inp_list[i]]=result_dict[inp_list[i]]+1
        else:
            result_dict[inp_list[i]]=1
    return result_dict  
