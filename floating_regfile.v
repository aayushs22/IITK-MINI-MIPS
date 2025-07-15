`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company:
// Engineer:
//
// Create Date: 04/16/2025 02:23:19 PM
// Design Name:
// Module Name: floating_regfile
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


module floating_regfile(
    input [4:0] f_read_addr1, input [4:0] f_read_addr2,
    input [31:0] f_data,input [31:0] f_data2, input f_WE,input f_WE2, input clk,
    input [4:0] f_write_addr,input [4:0] f_write_addr2,
    output [31:0] f_read1, output [31:0] f_read2
);
    reg [31:0] f_reg_file [31:0];

    assign f_read1 = f_reg_file[f_read_addr1];
    assign f_read2 = f_reg_file[f_read_addr2];

    initial begin
        f_reg_file[0] <= 32'b01000000011000000000000000000000;
        f_reg_file[1] <= 32'b00111111101000000000000000000000;
        f_reg_file[2] <= 32'b01000000000011100001010001111011;
        f_reg_file[3] <= 32'h0000000c;

        f_reg_file[22] <= 32'h00000000;//ZERO register
    end
    always @(posedge clk) begin
        if (f_WE) begin
            f_reg_file[f_write_addr] <= f_data;
        end
        if (f_WE2) begin
            f_reg_file[f_write_addr2] <= f_data2;
        end
    end
endmodule