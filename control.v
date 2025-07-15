`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company:
// Engineer:
//
// Create Date: 04/09/2025 02:31:28 PM
// Design Name:
// Module Name: control
// Project Name:
// Target Devices:
// Tool Versions:
// Description:
//
// Dependencies:
//
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
//
//////////////////////////////////////////////////////////////////////////////////

module control_unit(input clk,input[14:0]PC,output PC_control, output [14:0]j_instr_addr);
     //reg  [14:0] PC;
     wire [31:0] instr;

      instr_fetch iuf (.addr(PC), .instr(instr));

     //wire PC_control;
     //wire [14:0]j_instr_addr;
     //wire pc_temp;




      //wire [31:0]rs_value;
      wire [31:0]r1_value;
      wire [31:0]r2_value;

      wire [4:0]read_addr1;
      wire [4:0]read_addr2;
      wire [4:0]write_addr;
      wire WE;
      wire [31:0]data;

      wire [4:0]write_addr2;
      wire WE2;
      wire [31:0]data2;


     register_file rf(
    .read_addr1(read_addr1),.read_addr2(read_addr2),
    .data(data), .data2(data2), .WE(WE), .WE2(WE2), .clk(clk),
    .write_addr(write_addr),.write_addr2(write_addr2),
    .read1(r1_value),.read2(r2_value)
);

    wire [31:0]f_r1_value;
      wire [31:0]f_r2_value;

      wire [4:0]f_read_addr1;
      wire [4:0]f_read_addr2;
      wire [4:0]f_write_addr;
      wire f_WE;
      wire [31:0]f_data;

      wire [4:0]f_write_addr2;
      wire f_WE2;
      wire [31:0]f_data2;


     floating_regfile fl_rf(
    .f_read_addr1(f_read_addr1),.f_read_addr2(f_read_addr2),
    .f_data(f_data), .f_data2(f_data2), .f_WE(f_WE), .f_WE2(f_WE2), .clk(clk),
    .f_write_addr(f_write_addr),.f_write_addr2(f_write_addr2),
    .f_read1(f_r1_value),.f_read2(f_r2_value)
);
      wire [5:0]alu_operation;
      wire [31:0]alu_output;
      wire [31:0]alu_output2;
      wire [31:0]alu_input1;
      wire [31:0]alu_input2;
      wire is_zero;

     alu ALU_inst(.alu_operation(alu_operation),.input1(alu_input1),.input2(alu_input2),.output1(alu_output),.output2(alu_output2),.is_zero(is_zero));

      wire [5:0]f_alu_operation;
      wire [31:0]f_alu_output;
      wire [31:0]f_alu_output2;
      wire [31:0]f_alu_input1;
      wire [31:0]f_alu_input2;
      wire f_is_zero;

      floating_alu f_ALU_inst(.f_alu_operation(f_alu_operation),.f_input1(f_alu_input1),.f_input2(f_alu_input2),.f_output1(f_alu_output),.f_output2(f_alu_output2),.f_is_zero(f_is_zero));


     wire [14:0]data_read_addr;
     wire [31:0]data_mem_data;
     wire WE_data_mem;
     wire [14:0]mem_write_addr;
     wire [31:0]mem_read;


    data_mem dm(
    .read_addr(data_read_addr),
    .data(data_mem_data),.WE(WE_data_mem), .clk(clk),
    .write_addr(mem_write_addr),
    .read(mem_read)
);
    assign data_read_addr =
    (instr[31:26] == 6'b001110)                              ? alu_output :
    32'h00000000;

     assign data_mem_data =
    (instr[31:26] == 6'b001111)                              ? r2_value :
    32'h00000000;

     assign mem_write_addr=
    (instr[31:26] == 6'b001111)                              ? alu_output :
    32'h00000000;

    assign WE_data_mem=
    (instr[31:26] == 6'b001111)                              ? 1'b1 :
    1'b0;


     // assign j_instr_addr=instr[14:0];

    assign j_instr_addr =
    (instr[31:30] == 2'b01)                             ? instr[14:0] ://branches
    (instr[31:26] == 6'b011000)                         ? instr[14:0]://j
    (instr[31:26] == 6'b011001)                         ? r1_value[14:0]://jr
    (instr[31:26] == 6'b011010)                         ? instr[14:0]://jal
    15'b000000000000000;


   assign f_alu_operation = (instr[31:26] == 6'b110001) ? 6'b000001 : // add
                            (instr[31:26] == 6'b110010) ? 6'b000010 : // sub
                            (instr[31:26] == 6'b110011) ? 6'b000011 :
                            (instr[31:26] == 6'b110100) ? 6'b000100 :
                            (instr[31:26] == 6'b110101) ? 6'b000101 :
                            (instr[31:26] == 6'b110110) ? 6'b000110 :
                            (instr[31:26] == 6'b110111) ? 6'b000111 :

                            (instr[31:26] == 6'b111000) ? 6'b000001 : // mfc1
                            (instr[31:26] == 6'b111001) ? 6'b000001 : // mtc1
                            6'b000000; // default case

   assign alu_operation = (instr[31:26] == 6'b100001) ? 6'b000001 : // add
                       (instr[31:26] == 6'b100010) ? 6'b000010 : // sub
                       (instr[31:26] == 6'b100011) ? 6'b000011 : // and
                       (instr[31:26] == 6'b100100) ? 6'b000100 : // or
                       (instr[31:26] == 6'b100101) ? 6'b000101 : // not
                       (instr[31:26] == 6'b100110) ? 6'b000110 : // xor
                       (instr[31:26] == 6'b000001) ? 6'b000001 : // addi
                       (instr[31:26] == 6'b000010) ? 6'b000010 : // subi
                       (instr[31:26] == 6'b000011) ? 6'b000011 : // andi
                       (instr[31:26] == 6'b000100) ? 6'b000100 : // ori
                       (instr[31:26] == 6'b000110) ? 6'b000110 : // xori
                       (instr[31:26] == 6'b010000) ? 6'b000010 : // branch instructions, subtract
                       (instr[31:26] == 6'b010001) ? 6'b000010 : // branch instructions, subtract
                       (instr[31:26] == 6'b010010) ? 6'b000010 : // branch instructions, subtract
                       (instr[31:26] == 6'b010011) ? 6'b000010 : // branch instructions, subtract
                       (instr[31:26] == 6'b010100) ? 6'b000010 : // branch instructions, subtract
                       (instr[31:26] == 6'b010101) ? 6'b000010 : // branch instructions, subtract
                       (instr[31:26] == 6'b010110) ? 6'b000010 : // branch instructions, unsigned subtract
                       (instr[31:26] == 6'b010111) ? 6'b000010 : // branch instructions, unsigned subtract
                       (instr[31:26] == 6'b001000) ? 6'b000111 : // sll, i-type
                       (instr[31:26] == 6'b001001) ? 6'b001000 : // srl
                       (instr[31:26] == 6'b001010) ? 6'b000111 : // sla
                       (instr[31:26] == 6'b001011) ? 6'b001000 : // sra
                       (instr[31:26] == 6'b101100) ? 6'b001001 : // slt
                       (instr[31:26] == 6'b001100) ? 6'b001001 : // slti
                       (instr[31:26] == 6'b001101) ? 6'b001010 : // seq
                       (instr[31:26] == 6'b101101) ? 6'b001011 : // mul

                       (instr[31:26] == 6'b001110) ? 6'b000001 : // lw//r1=mem[r0+const]
                       (instr[31:26] == 6'b001111) ? 6'b000001 : // sw//mem[r0+const]=r1

                       // lui->pseudo instr





                       6'b000000; // default case


   assign PC_control =
    (instr[31] == 1'b1)                             ? 1'b0 :
    (instr[31:30] == 2'b00)                             ? 1'b0 :
    (instr[31:26] == 6'b010000 && alu_output == 32'b0)              ? 1'b1 :
    (instr[31:26] == 6'b010001 && alu_output != 32'b0)              ? 1'b1 :
    (instr[31:26] == 6'b010010 && $signed(alu_output) > 0)          ? 1'b1 :
    (instr[31:26] == 6'b010011 && $signed(alu_output) >= 0)         ? 1'b1 :
    (instr[31:26] == 6'b010100 && $signed(alu_output) < 0)          ? 1'b1 :
    (instr[31:26] == 6'b010101 && $signed(alu_output) <= 0)         ? 1'b1 :
    (instr[31:26] == 6'b010110 && $signed(alu_output) < 0)          ? 1'b1 :
    (instr[31:26] == 6'b010111 && $signed(alu_output) > 0)          ? 1'b1 :

    (instr[31:26] == 6'b011000)          ? 1'b1 :
    (instr[31:26] == 6'b011001)          ? 1'b1 :
    (instr[31:26] == 6'b011010)          ? 1'b1 :


    1'b0;

   assign WE =
   (instr[31:30] == 6'b11)                      ? 1'b0://other floating point instructiuons
   (instr[31:26] == 6'b111000)                      ? 1'b1://mfc1
   (instr[31:26] == 6'b001111)                      ? 1'b0://sw
    (instr[31] == 1'b1)                             ? 1'b1 :
    (instr[31:30] == 2'b00)                             ? 1'b1 :
    (instr[31:26] == 6'b011010)                          ? 1'b1 : //jal
    1'b0;

   assign WE2 =
    (instr[31:26] ==  6'b101101)                          ? 1'b1 : //mul

    1'b0;

    assign write_addr =
    (instr[31:26] ==  6'b101101)                     ? 5'b11000 :
    (instr[31] == 1'b1)                             ? instr[15:11] :
    (instr[31:30] == 2'b00)                             ? instr[20:16] :
    (instr[31:26] == 6'b011010)                         ? 5'b11111:
    5'b00000;

    assign write_addr2 =
    (instr[31:26] ==  6'b101101)                     ? 5'b11001 :
    5'b00000;

    assign read_addr1 =
    (instr[31:26] == 6'b111001)                     ? instr[25:21] : // mtc1
    (instr[31] == 1'b1)                             ? instr[25:21] :
    (instr[31:30] == 2'b01)                             ? instr[25:21] :
    (instr[31:30] == 2'b00)                             ? instr[25:21] :
    (instr[31:26] == 6'b011001)                         ? instr[25:21] :
    5'b00000;

    assign read_addr2 =
    (instr[31:26] == 6'b001111)                     ? instr[20:16] ://sw
    (instr[31] == 1'b1)                             ? instr[20:16] :
    (instr[31:30] == 2'b01)                             ? instr[20:16] :
    5'b00000;

    assign alu_input1 =
    (instr[31] == 1'b1)                             ? r1_value :
    (instr[31:30] == 2'b01)                             ? r1_value :
    (instr[31:30] == 2'b00)                             ? r1_value :
    32'h00000000;

    assign alu_input2 =
    (instr[31] == 1'b1)                             ? r2_value :
    (instr[31:30] == 2'b01)                             ? r2_value :
    (instr[31:30] == 2'b00)                             ? instr[15:0] :
    32'h00000000;

    assign data =
    (instr[31:26] == 6'b111000)                      ? f_alu_output://mfc1
    (instr[31:26] == 6'b001110)                     ? mem_read://lw
    (instr[31] == 1'b1)                             ? alu_output :
    (instr[31:30] == 2'b00)                             ? alu_output :
    (instr[31:26] == 6'b011010)                         ? PC:
    32'h00000000;

     assign data2 =

   (instr[31:26] ==  6'b101101)                          ? alu_output2 : //mul
    32'h00000000;



    //floating point
    assign f_WE =
    (instr[31:26] == 6'b111000)                      ? 1'b0://mfc1
   (instr[31:30] == 2'b11)                      ? 1'b1://r-type floating
    1'b0;

   assign f_WE2 =

    1'b0;

    assign f_write_addr =
    (instr[31:30] == 2'b11)                      ? instr[15:11]://r-type floating
    5'b00000;

    assign write_addr2 =
    5'b00000;

    assign f_read_addr1 =
    (instr[31:30] == 2'b11)                      ? instr[25:21]://r-type floating

    5'b00000;

    assign f_read_addr2 =
    (instr[31:30] == 2'b11)                      ? instr[20:16]://r-type floating
    5'b00000;

    assign f_data =

    (instr[31:30] == 2'b11)                          ? f_alu_output :
    32'h00000000;

     assign f_data2 =
    32'h00000000;

    assign f_alu_input1 =
    (instr[31:26] == 6'b111001)                     ? r1_value: // mtc1
    (instr[31:30] == 2'b11)                             ? f_r1_value :
    32'h00000000;

    assign f_alu_input2 =
    (instr[31:30] == 2'b11)                             ? f_r2_value :
    32'h00000000;

  //end
//PC_incr pci(.PC_control(PC_control),.j_instr_addr(j_instr_addr),.PC(PC),.clk(clk),.PC_out(PC));
endmodule
