# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import dxfcreate
import ezdxf

import struct
import binascii

import itertools


def encode_id(x, y, line_type, element_id, pin_id):
    # 首先，验证输入是否符合给定的位大小
    if not (0 <= x < 2**16):
        raise ValueError("x should be in range [0, 2^16-1]")
    if not (0 <= y < 2**16):
        raise ValueError("y should be in range [0, 2^16-1]")
    if not (0 <= line_type < 2**4):
        raise ValueError("line_type should be in range [0, 2^4-1]")
    if not (0 <= element_id < 2**12):
        raise ValueError("element_id should be in range [0, 2^12-1]")
    if not (0 <= pin_id < 2**16):
        raise ValueError("pin_id should be in range [0, 2^16-1]")

    # 根据位数进行左移操作
    result = x
    result = (result << 16) | y
    result = (result << 4) | line_type
    result = (result << 12) | element_id
    result = (result << 16) | pin_id

    # 转换为十六进制表示
    hex_representation = hex(result)
    return hex_representation, result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # csv_filename = "./config/TC2.2/EdgeLine_NS_L12.csv"
    # blocks_data_list = []
    # with open(csv_filename, newline='') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         blocks_data_list.append(row)
    #
    # dxf = dxfcreate.DxfCreate()
    #
    # # dxf.create_SWH(blocks_data_list)
    # # dxf.create_directLine_block(blocks_data_list)
    # # dxf.create_LWPolyLineL1(blocks_data_list)
    # # dxf.create_LWPolyLineL2(blocks_data_list)
    # # dxf.create_LWPolyLineL4(blocks_data_list)
    # # dxf.create_LWPolyLineL6(blocks_data_list)
    # # dxf.create_LWPolyLineL12(blocks_data_list)
    # # dxf.create_EdgeLineL1(blocks_data_list)
    # # dxf.create_EdgeLineL2(blocks_data_list)
    # # dxf.create_EdgeLineL4(blocks_data_list)
    # # dxf.create_EdgeLineL6(blocks_data_list)
    # dxf.create_EdgeLineL12(blocks_data_list)
    #
    # dxf.save_as(f"./result/TC2.2/EdgeLine_NS_L12.dxf")

    dwg = ezdxf.new(dxfversion='AC1021')
    msp = dwg.modelspace()

    block1 = dwg.blocks.new(name="circle.a")
    block1.add_circle((0, 0), 2)
    block_ref = msp.add_blockref("circle.a", (0, 0))
    #
    # # integer_data = 1234567890
    # # binary_data2 = format(integer_data, '032b')
    # # binary_data3 = struct.pack("<I", integer_data)
    # # print("32位的二进制数据:", binary_data2)
    # # print("32位的二进制数据字节串:", binary_data3)
    # # logic_column = 150
    # # logic_row = 360
    # # encoded_data = (logic_column & 0xFFFFFFFF) << 32 | (logic_row & 0xFFFFFFFF)
    # # binary_data4 = struct.pack("<Q", encoded_data)
    # # binary_encoded_data = format(encoded_data, '064b')
    # # print("64位的二进制数据:", binary_encoded_data)
    # # print("64位的二进制数据字节串:", binary_data4)
    # # print("64位的二进制编码:", bin(encoded_data))
    #
    # # binary_data = b"\x00\x00\x00\x00"
    # # hex_string = "0x12A3"
    # # hex_bytes = b'\x12\xa3'
    # # hex_bytearray = bytearray([0x12, 0xA3])
    # #
    # # print(binary_data)
    # # print(hex_string)
    # # print(hex_bytes)
    # # print(hex_bytearray)
    #
    encoded_hex, encoded_int = encode_id(1, 2, 3, 4, 5)
    print(f"Hex Representation: {encoded_hex}")
    print(f"Integer Representation: {encoded_int}")
    binary_representation = format(encoded_int, '064b')
    hex_bytes = encoded_int.to_bytes(8, byteorder='big')
    print(binary_representation)
    print(hex_bytes)

    block_ref.set_xdata("ref_test", [(1004, hex_bytes)])
    # # block_ref.set_xdata("ref_test", [(1071, [(1070, 150), (1070, 160)])])
    # # block1.block.set_xdata("test", [(1070, 105), (1001, 106), (1070, 106)])
    # # block1.block.set_xdata("app", [(1001, 106)])
    # block2 = dwg.blocks.get("circle.a")
    tags = block_ref.get_xdata("ref_test")
    print(block_ref.dxf.name, tags)
    # tags = block2.block.get_xdata("test")
    # print(block2.name, tags)
    print(tags[0][1])
    hex_bytes_tra = tags[0][1]
    int_value = int.from_bytes(hex_bytes_tra, byteorder='big')
    int_a = 4222945286094849
    binary_str = format(int_a, '064b')
    print(int_value)
    print(binary_str)
    # dwg.saveas(filename="./double_xdata.dxf")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
