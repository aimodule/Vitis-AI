# line numbers of input and output tensors (order like in protoxt)
input_tensor_line_numbers = [16, 209, 173, 245, 283, 321]
output_tensor_line_numbers = [196, 232, 270, 308, 346, 197, 233, 271, 309, 347, 199, 235, 273, 311, 349, 198, 234, 272, 310, 348]
tensor_order_compile_params = [16, 17, 18, 20, 19, 9, 4, 10, 5, 7, 2, 15, 13, 12, 11, 8, 3, 6, 1, 14]

# load nndct auto-generated file
file_path = "quantize_result/SOLO.py"
with open(file_path) as param_file:
    lines = param_file.readlines()

# read lines
if len(lines) == 712:
    # add an empty line 0 that line numbers match with list entries
    lines.insert(0, '')
else:
    raise Exception("Wrong formatted param file.")
    
# function for deleting \n from strings and replacing . with _
def proc_str(value):
    proc = ''.join(value.splitlines())
    ret = proc.replace(".", "_")
    return ret

# input tensors
input_tensors = []
for ln in input_tensor_line_numbers:
    line = lines[ln].split("/")
    tensor = proc_str(line[len(line)-1])
    input_tensors.append(tensor)

# output tensors
output_tensors = []
for ln in output_tensor_line_numbers:
    line = lines[ln].split("/")
    tensor = proc_str(line[len(line)-1])
    output_tensors.append(tensor)

# prototxt
begin = 'model {\n\tname : "solo" \n\tkernel {\n\t\tname: "solo_0"\n\t\tmean: 103.53\n\t\tmean: 116.28\n\t\tmean: 123.675\n\t\tscale: 0.01742919\n\t\tscale: 0.017507\n\t\tscale: 0.01712475\n\t}\n\tsolo_param {\n'
end = '\n\t\tscore_thr: 0.3\n\t\tmask_thr: 0.5\n\t\tnms_pre: 200\n\t\tupdate_thr: 0.05\n\t\tmax_per_img: 25\n\t}\n}'

with open("solo_pt/solo_pt.prototxt", "w") as f:
    f.write(begin)
    for tensor in input_tensors:
        f.write('\t\tinput_tensor_name: "' + tensor + '"\n')
    for tensor in output_tensors:
        f.write('\t\toutput_tensor_name: "' + tensor + '"\n')
    f.write(end)

# compile params
compile_params = '{"output_ops":"'
cnt = 0
for idx in tensor_order_compile_params:
    cnt = cnt + 1
    compile_params = compile_params + 'SOLO__SOLO_DecoupledSOLOLightHead_bbox_head__' + output_tensors[idx-1] + '_fix'
    if cnt < len(output_tensor_line_numbers):
        compile_params = compile_params + ','
compile_params = compile_params + '"}'
print(compile_params)
