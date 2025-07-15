
`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company:
// Engineer:
//
// Create Date: 04/16/2025 02:33:29 PM
// Design Name:
// Module Name: floating_alu
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
module fp_adder(
    input  [31:0] a,
    input  [31:0] b,
    output reg [31:0] sum
);

  reg         a_sign, b_sign;
  reg [7:0]   a_exp,  b_exp;
  reg [22:0]  a_frac, b_frac;
  reg [23:0]  a_mant, b_mant;

  reg         op1_sel;
  reg         op1_sign, op2_sign;
  reg [7:0]   exp_large;
  reg [23:0]  op1_mant, op2_mant;
  reg [7:0]   exp_diff;

  reg [27:0]  op1_ext, op2_ext;
  reg [27:0]  mant_sum;
  reg         result_sign;

  reg [27:0]  mant_norm;     // Normalized mantissa
  reg [7:0]   exp_result;    // Adjusted exponent after normalization
  integer i;
  integer found;           // Flag to indicate first '1' found
  integer shift;           // Number of positions to shift for normalization

  // Rounding signals
  reg [23:0]  mantissa_final; // 24-bit mantissa (1 implicit bit + 23 fraction bits)
  reg [2:0]   round_bits;     // Guard, round, and sticky bits

  // Main combinational block
  always @(*) begin
    // 1. Extract the fields of both operands.
    a_sign = a[31];
    b_sign = b[31];
    a_exp  = a[30:23];
    b_exp  = b[30:23];
    a_frac = a[22:0];
    b_frac = b[22:0];

    // For normalized numbers, the implicit MSB is 1.
    a_mant = (a_exp == 0) ? {1'b0, a_frac} : {1'b1, a_frac};
    b_mant = (b_exp == 0) ? {1'b0, b_frac} : {1'b1, b_frac};

    // 2. Determine which operand has the larger magnitude.
    if ((a_exp > b_exp) || ((a_exp == b_exp) && (a_mant >= b_mant))) begin
      op1_sel   = 1;        // A is larger
      op1_sign  = a_sign;
      op2_sign  = b_sign;
      exp_large = a_exp;
      op1_mant  = a_mant;
      op2_mant  = b_mant;
      exp_diff  = a_exp - b_exp;
    end
    else begin
      op1_sel   = 0;        // B is larger
      op1_sign  = b_sign;
      op2_sign  = a_sign;
      exp_large = b_exp;
      op1_mant  = b_mant;
      op2_mant  = a_mant;
      exp_diff  = b_exp - a_exp;
    end

    // 3. Align the mantissas.
    // Extend 24-bit mantissas to 28 bits: one extra MSB and 3 LSB guard bits.
    op1_ext = {1'b0, op1_mant, 3'b000};
    op2_ext = {1'b0, op2_mant, 3'b000} >> exp_diff;

    // 4. Perform addition or subtraction.
    if (op1_sign == op2_sign) begin
      mant_sum    = op1_ext + op2_ext;
      result_sign = op1_sign;  // Same sign: straightforward addition.
    end
    else begin
      // Subtraction: since op1 is the larger magnitude, subtract op2 from op1.
      mant_sum    = op1_ext - op2_ext;
      result_sign = op1_sign;
    end

    // 5. Normalize the result.
    if (mant_sum[27] == 1'b1) begin
      // If there's a carry-out, shift right by 1 and increment the exponent.
      mant_norm  = mant_sum >> 1;
      exp_result = exp_large + 1;
    end
    else begin
      if (mant_sum != 0) begin
        shift = 0;
        found = 0;        // Initialize the flag.
        mant_norm = mant_sum;
        // Find the position of the first '1' in bits [26:0]
        for (i = 26; i >= 0; i = i - 1) begin
          if (!found && mant_norm[i] == 1'b1) begin
            shift = 26 - i;
            found = 1;  // Mark that the first '1' has been found.
          end
        end
        mant_norm  = mant_norm << shift;
        exp_result = exp_large - shift;
      end
      else begin
        // If the result is zero.
        mant_norm  = 0;
        exp_result = 0;
      end
    end

    // 6. Rounding: use bits [26:3] for the 24-bit mantissa; bits [2:0] are for rounding.
    mantissa_final = mant_norm[26:3];
    round_bits     = mant_norm[2:0];

    // Round-to-nearest, ties-to-even.
    if ((round_bits > 3'b100) ||
        ((round_bits == 3'b100) && (mantissa_final[0] == 1'b1))) begin
      mantissa_final = mantissa_final + 1;
      // Handle rounding overflow (e.g., rounding causes a carry).
      if (mantissa_final == 24'h800000) begin
        mantissa_final = mantissa_final >> 1;
        exp_result = exp_result + 1;
      end
    end

    // 7. Pack the result into IEEE-754 format.
    // Drop the implicit bit: use lower 23 bits of mantissa_final.
    sum = {result_sign, exp_result, mantissa_final[22:0]};
  end

endmodule

module floating_alu(
    input [5:0] f_alu_operation,
    input [31:0] f_input1,
    input [31:0] f_input2,
    output [31:0] f_output1,
    output [31:0] f_output2,
    output f_is_zero
);
wire[31:0] f_added;
wire [31:0]b;
    fp_adder fpa(
    .a(f_input1),
    .b(b) ,
    .sum(f_added)
);
    assign b= (f_alu_operation == 6'd1) ?  f_input2:
              (f_alu_operation == 6'd2) ?  {1'd1,f_input2[30:0]}:
              {1'd1,f_input2[30:0]};


    assign f_output1 = (f_alu_operation == 6'd1) ? (f_added) :
                     (f_alu_operation == 6'd2) ? (f_added) :
                     (f_alu_operation == 6'b000011 && f_added==32'd0) ?  (32'd1):
                     (f_alu_operation == 6'b000100 && (f_added==32'd0 ||f_added[31]==1'b1) )? (32'd1) :
                     (f_alu_operation == 6'b000101 && (f_added[31]==1'b1)) ? (32'd1) :
                     (f_alu_operation == 6'b000110 && (f_added==32'd0 ||f_added[31]==1'b0) ) ? (32'd1) :
                     (f_alu_operation == 6'b000111 && (f_added!=32'd0 ||f_added[31]==1'b0) ) ? (32'd1) :
                     32'h00000000;

    assign output2 = 32'h00000000;
    assign f_is_zero = (f_output1 == 32'h00000000) ? 1'b1 : 1'b0;
endmodule