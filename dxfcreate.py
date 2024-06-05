import ezdxf
from ezdxf.addons import Importer


class DxfCreate:
    def __init__(self):
        self.dwg = ezdxf.new(dxfversion='AC1021')
        self.msp = self.dwg.modelspace()

    def save_as(self, filename: str):
        self.dwg.saveas(filename=filename)

    def import_block(self, sourcedwgs: list):
        for dwg in sourcedwgs:
            importer = Importer(dwg, self.dwg)
            importer.import_blocks(self.get_blocks_name(dwg))
            importer.finalize()

    def get_blocks_name(self, dwg) -> list:
        block_name_list = []
        for e in dwg.blocks:
            if e.name != "*Model_Space" and e.name != "*Paper_Space":
                block_name_list.append(e.name)
        return block_name_list

    def add_block_refs(self):
        for item_regions in self.config.get_items_region():
            for region in item_regions.get_regions():
                for point in region.get_logic_points():
                    block_ref = self.msp.add_blockref(
                        item_regions.get_item_type(),
                        (
                            point.get_column() * self.config.get_columns_width(),
                            point.get_row() * self.config.get_rows_height()
                        )
                    )

    def create_SWH(self, block_pins: list):
        self.msp.add_line((0, 0), (0, 2000))
        self.msp.add_line((0, 2000), (2000, 2000))
        self.msp.add_line((2000, 2000), (2000, 0))
        self.msp.add_line((2000, 0), (0, 0))
        for data in block_pins:
            pin_name = data["block_name"]
            x = float(data["x"])
            y = float(data["y"])
            pin_block = self.dwg.blocks.new(name=pin_name)
            pin_block.add_circle((0, 0), 2)
            self.msp.add_blockref(pin_name, (x, y))

    def create_directLine_block(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            end_x = float(data["end_x"])
            end_y = float(data["end_y"])
            line_block = self.dwg.blocks.new(name=line_name)
            line_block.add_line((0, 0), (end_x, end_y))

    def create_LWPolyLineL1(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            x_0 = float(data["x_0"])
            y_0 = float(data["y_0"])
            x_1 = float(data["x_1"])
            y_1 = float(data["y_1"])
            x_2 = float(data["x_2"])
            y_2 = float(data["y_2"])
            x_3 = float(data["x_3"])
            y_3 = float(data["y_3"])
            points = [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3)]
            lwpolyline_block = self.dwg.blocks.new(name=line_name)
            lwpolyline_block.add_lwpolyline(points)
            self.msp.add_blockref(line_name, (0,0))

    def create_LWPolyLineL2(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            x_0 = float(data["x_0"])
            y_0 = float(data["y_0"])
            x_1 = float(data["x_1"])
            y_1 = float(data["y_1"])
            x_2 = float(data["x_2"])
            y_2 = float(data["y_2"])
            x_3 = float(data["x_3"])
            y_3 = float(data["y_3"])
            x_4 = float(data["x_4"])
            y_4 = float(data["y_4"])
            x_5 = float(data["x_5"])
            y_5 = float(data["y_5"])
            points = [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5)]
            lwpolyline_block = self.dwg.blocks.new(name=line_name)
            lwpolyline_block.add_lwpolyline(points)
            self.msp.add_blockref(line_name, (0, 0))

    def create_LWPolyLineL4(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            x_0 = float(data["x_0"])
            y_0 = float(data["y_0"])
            x_1 = float(data["x_1"])
            y_1 = float(data["y_1"])
            x_2 = float(data["x_2"])
            y_2 = float(data["y_2"])
            x_3 = float(data["x_3"])
            y_3 = float(data["y_3"])
            x_4 = float(data["x_4"])
            y_4 = float(data["y_4"])
            x_5 = float(data["x_5"])
            y_5 = float(data["y_5"])
            x_6 = float(data["x_6"])
            y_6 = float(data["y_6"])
            x_7 = float(data["x_7"])
            y_7 = float(data["y_7"])
            x_8 = float(data["x_8"])
            y_8 = float(data["y_8"])
            x_9 = float(data["x_9"])
            y_9 = float(data["y_9"])
            points = [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6), (x_7, y_7), (x_8, y_8), (x_9, y_9)]
            lwpolyline_block = self.dwg.blocks.new(name=line_name)
            lwpolyline_block.add_lwpolyline(points)
            self.msp.add_blockref(line_name, (0, 0))

    def create_LWPolyLineL6(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            x_0 = float(data["x_0"])
            y_0 = float(data["y_0"])
            x_1 = float(data["x_1"])
            y_1 = float(data["y_1"])
            x_2 = float(data["x_2"])
            y_2 = float(data["y_2"])
            x_3 = float(data["x_3"])
            y_3 = float(data["y_3"])
            x_4 = float(data["x_4"])
            y_4 = float(data["y_4"])
            x_5 = float(data["x_5"])
            y_5 = float(data["y_5"])
            x_6 = float(data["x_6"])
            y_6 = float(data["y_6"])
            x_7 = float(data["x_7"])
            y_7 = float(data["y_7"])
            x_8 = float(data["x_8"])
            y_8 = float(data["y_8"])
            x_9 = float(data["x_9"])
            y_9 = float(data["y_9"])
            x_10 = float(data["x_10"])
            y_10 = float(data["y_10"])
            x_11 = float(data["x_11"])
            y_11 = float(data["y_11"])
            x_12 = float(data["x_12"])
            y_12 = float(data["y_12"])
            x_13 = float(data["x_13"])
            y_13 = float(data["y_13"])
            points = [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6), (x_7, y_7),
                      (x_8, y_8), (x_9, y_9), (x_10, y_10), (x_11, y_11), (x_12, y_12), (x_13, y_13)]
            lwpolyline_block = self.dwg.blocks.new(name=line_name)
            lwpolyline_block.add_lwpolyline(points)

    def create_LWPolyLineL12(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            x_0 = float(data["x_0"])
            y_0 = float(data["y_0"])
            x_1 = float(data["x_1"])
            y_1 = float(data["y_1"])
            x_2 = float(data["x_2"])
            y_2 = float(data["y_2"])
            x_3 = float(data["x_3"])
            y_3 = float(data["y_3"])
            x_4 = float(data["x_4"])
            y_4 = float(data["y_4"])
            x_5 = float(data["x_5"])
            y_5 = float(data["y_5"])
            x_6 = float(data["x_6"])
            y_6 = float(data["y_6"])
            x_7 = float(data["x_7"])
            y_7 = float(data["y_7"])
            x_8 = float(data["x_8"])
            y_8 = float(data["y_8"])
            x_9 = float(data["x_9"])
            y_9 = float(data["y_9"])
            x_10 = float(data["x_10"])
            y_10 = float(data["y_10"])
            x_11 = float(data["x_11"])
            y_11 = float(data["y_11"])
            x_12 = float(data["x_12"])
            y_12 = float(data["y_12"])
            x_13 = float(data["x_13"])
            y_13 = float(data["y_13"])
            x_14 = float(data["x_14"])
            y_14 = float(data["y_14"])
            x_15 = float(data["x_15"])
            y_15 = float(data["y_15"])
            x_16 = float(data["x_16"])
            y_16 = float(data["y_16"])
            x_17 = float(data["x_17"])
            y_17 = float(data["y_17"])
            x_18 = float(data["x_18"])
            y_18 = float(data["y_18"])
            x_19 = float(data["x_19"])
            y_19 = float(data["y_19"])
            x_20 = float(data["x_20"])
            y_20 = float(data["y_20"])
            x_21 = float(data["x_21"])
            y_21 = float(data["y_21"])
            x_22 = float(data["x_22"])
            y_22 = float(data["y_22"])
            x_23 = float(data["x_23"])
            y_23 = float(data["y_23"])
            x_24 = float(data["x_24"])
            y_24 = float(data["y_24"])
            x_25 = float(data["x_25"])
            y_25 = float(data["y_25"])
            points = [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6), (x_7, y_7),
                      (x_8, y_8), (x_9, y_9), (x_10, y_10), (x_11, y_11), (x_12, y_12), (x_13, y_13), (x_14, y_14),
                      (x_15, y_15), (x_16, y_16), (x_17, y_17), (x_18, y_18), (x_19, y_19), (x_20, y_20),
                      (x_21, y_21), (x_22, y_22), (x_23, y_23), (x_24, y_24), (x_25, y_25)]
            lwpolyline_block = self.dwg.blocks.new(name=line_name)
            lwpolyline_block.add_lwpolyline(points)

    def create_EdgeLineL1(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            x_0 = float(data["x_0"])
            y_0 = float(data["y_0"])
            x_1 = float(data["x_1"])
            y_1 = float(data["y_1"])
            x_2 = float(data["x_2"])
            y_2 = float(data["y_2"])
            x_3 = float(data["x_3"])
            y_3 = float(data["y_3"])
            x_4 = float(data["x_4"])
            y_4 = float(data["y_4"])
            x_5 = float(data["x_5"])
            y_5 = float(data["y_5"])
            points = [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5)]
            lwpolyline_block = self.dwg.blocks.new(name=line_name)
            lwpolyline_block.add_lwpolyline(points)

    def create_EdgeLineL2(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            x_0 = float(data["x_0"])
            y_0 = float(data["y_0"])
            x_1 = float(data["x_1"])
            y_1 = float(data["y_1"])
            x_2 = float(data["x_2"])
            y_2 = float(data["y_2"])
            x_3 = float(data["x_3"])
            y_3 = float(data["y_3"])
            x_4 = float(data["x_4"])
            y_4 = float(data["y_4"])
            x_5 = float(data["x_5"])
            y_5 = float(data["y_5"])
            x_6 = float(data["x_6"])
            y_6 = float(data["y_6"])
            x_7 = float(data["x_7"])
            y_7 = float(data["y_7"])
            points = [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6), (x_7, y_7)]
            lwpolyline_block = self.dwg.blocks.new(name=line_name)
            lwpolyline_block.add_lwpolyline(points)

    def create_EdgeLineL4(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            x_0 = float(data["x_0"])
            y_0 = float(data["y_0"])
            x_1 = float(data["x_1"])
            y_1 = float(data["y_1"])
            x_2 = float(data["x_2"])
            y_2 = float(data["y_2"])
            x_3 = float(data["x_3"])
            y_3 = float(data["y_3"])
            x_4 = float(data["x_4"])
            y_4 = float(data["y_4"])
            x_5 = float(data["x_5"])
            y_5 = float(data["y_5"])
            x_6 = float(data["x_6"])
            y_6 = float(data["y_6"])
            x_7 = float(data["x_7"])
            y_7 = float(data["y_7"])
            x_8 = float(data["x_8"])
            y_8 = float(data["y_8"])
            x_9 = float(data["x_9"])
            y_9 = float(data["y_9"])
            x_10 = float(data["x_10"])
            y_10 = float(data["y_10"])
            x_11 = float(data["x_11"])
            y_11 = float(data["y_11"])
            points = [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6), (x_7, y_7),
                      (x_8, y_8), (x_9, y_9), (x_10, y_10), (x_11, y_11)]
            lwpolyline_block = self.dwg.blocks.new(name=line_name)
            lwpolyline_block.add_lwpolyline(points)

    def create_EdgeLineL6(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            x_0 = float(data["x_0"])
            y_0 = float(data["y_0"])
            x_1 = float(data["x_1"])
            y_1 = float(data["y_1"])
            x_2 = float(data["x_2"])
            y_2 = float(data["y_2"])
            x_3 = float(data["x_3"])
            y_3 = float(data["y_3"])
            x_4 = float(data["x_4"])
            y_4 = float(data["y_4"])
            x_5 = float(data["x_5"])
            y_5 = float(data["y_5"])
            x_6 = float(data["x_6"])
            y_6 = float(data["y_6"])
            x_7 = float(data["x_7"])
            y_7 = float(data["y_7"])
            x_8 = float(data["x_8"])
            y_8 = float(data["y_8"])
            x_9 = float(data["x_9"])
            y_9 = float(data["y_9"])
            x_10 = float(data["x_10"])
            y_10 = float(data["y_10"])
            x_11 = float(data["x_11"])
            y_11 = float(data["y_11"])
            x_12 = float(data["x_12"])
            y_12 = float(data["y_12"])
            x_13 = float(data["x_13"])
            y_13 = float(data["y_13"])
            x_14 = float(data["x_14"])
            y_14 = float(data["y_14"])
            x_15 = float(data["x_15"])
            y_15 = float(data["y_15"])
            points = [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6), (x_7, y_7),
                      (x_8, y_8), (x_9, y_9), (x_10, y_10), (x_11, y_11), (x_12, y_12), (x_13, y_13), (x_14, y_14),
                      (x_15, y_15)]
            lwpolyline_block = self.dwg.blocks.new(name=line_name)
            lwpolyline_block.add_lwpolyline(points)

    def create_EdgeLineL12(self, block_lines: list):
        for data in block_lines:
            line_name = data["block_name"]
            x_0 = float(data["x_0"])
            y_0 = float(data["y_0"])
            x_1 = float(data["x_1"])
            y_1 = float(data["y_1"])
            x_2 = float(data["x_2"])
            y_2 = float(data["y_2"])
            x_3 = float(data["x_3"])
            y_3 = float(data["y_3"])
            x_4 = float(data["x_4"])
            y_4 = float(data["y_4"])
            x_5 = float(data["x_5"])
            y_5 = float(data["y_5"])
            x_6 = float(data["x_6"])
            y_6 = float(data["y_6"])
            x_7 = float(data["x_7"])
            y_7 = float(data["y_7"])
            x_8 = float(data["x_8"])
            y_8 = float(data["y_8"])
            x_9 = float(data["x_9"])
            y_9 = float(data["y_9"])
            x_10 = float(data["x_10"])
            y_10 = float(data["y_10"])
            x_11 = float(data["x_11"])
            y_11 = float(data["y_11"])
            x_12 = float(data["x_12"])
            y_12 = float(data["y_12"])
            x_13 = float(data["x_13"])
            y_13 = float(data["y_13"])
            x_14 = float(data["x_14"])
            y_14 = float(data["y_14"])
            x_15 = float(data["x_15"])
            y_15 = float(data["y_15"])
            x_16 = float(data["x_16"])
            y_16 = float(data["y_16"])
            x_17 = float(data["x_17"])
            y_17 = float(data["y_17"])
            x_18 = float(data["x_18"])
            y_18 = float(data["y_18"])
            x_19 = float(data["x_19"])
            y_19 = float(data["y_19"])
            x_20 = float(data["x_20"])
            y_20 = float(data["y_20"])
            x_21 = float(data["x_21"])
            y_21 = float(data["y_21"])
            x_22 = float(data["x_22"])
            y_22 = float(data["y_22"])
            x_23 = float(data["x_23"])
            y_23 = float(data["y_23"])
            x_24 = float(data["x_24"])
            y_24 = float(data["y_24"])
            x_25 = float(data["x_25"])
            y_25 = float(data["y_25"])
            x_26 = float(data["x_26"])
            y_26 = float(data["y_26"])
            x_27 = float(data["x_27"])
            y_27 = float(data["y_27"])
            points = [(x_0, y_0), (x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4), (x_5, y_5), (x_6, y_6), (x_7, y_7),
                      (x_8, y_8), (x_9, y_9), (x_10, y_10), (x_11, y_11), (x_12, y_12), (x_13, y_13), (x_14, y_14),
                      (x_15, y_15), (x_16, y_16), (x_17, y_17), (x_18, y_18), (x_19, y_19), (x_20, y_20), (x_21, y_21),
                      (x_22, y_22), (x_23, y_23), (x_24, y_24), (x_25, y_25), (x_26, y_26), (x_27, y_27)]
            lwpolyline_block = self.dwg.blocks.new(name=line_name)
            lwpolyline_block.add_lwpolyline(points)