`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/09/2025 02:42:20 PM
// Design Name: 
// Module Name: data_mem
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



module data_mem(
    input [14:0] read_addr,
    input [31:0] data, input WE, input clk,
    input [14:0] write_addr,
    output [31:0] read
);
    reg [31:0] data_mem [31:0];

    assign read = data_mem[read_addr];
  

    initial begin
        data_mem[3] <= 32'd5;
        data_mem[4] <= 32'd47;
        data_mem[5] <= 32'd5;
        data_mem[6] <= 32'd0;
        data_mem[7] <= 32'd55;
        data_mem[8] <= 32'd1;
    end
    always @(posedge clk) begin
        if (WE) begin
            data_mem[write_addr] <= data;
        end
    end
endmodule
