
library ieee;
use ieee.std_logic_1164.all;

entity control_unit is
port( start_writing, clk, rstn, UART_rx, tc_10_bit_cnt, tc_50_clk_cnt, tc_bittime_clk_cnt,
     tc_memsize_data_cnt : in std_logic;
     rdn_wr_data_ssram , en_addr_cnt , upn_down_addr_cnt , PISO_load , PISO_shift ,
     uart_tx_mux_sel , rstn_bit_cnt , en_bit_cnt , rstn_clk_cnt ,en_clk_cnt ,
     rstn_data_cnt , en_data_cnt : out std_logic);
end entity control_unit;


architecture behavioral of control_unit is
type state_type is (Idle , Waiting_for_data , Write_Memory, Read_Memory ,Load_REG ,Shift_Data_out,
                    Wait_Bit_Time);
signal Next_state , present_state : state_type;


begin
     Next_state_evaluation: process(present_state, start_writing, clk, rstn, UART_rx,
      tc_10_bit_cnt , tc_50_clk_cnt ,tc_bittime_clk_cnt ,tc_memsize_data_cnt)

     begin
     if rstn='0' then
      Next_state <=Idle;
     
          else
               Next_state <=Idle; --default
               case present_state is
     
               when Idle => case UART_rx is
                    when '0' => Next_state <=Read_Memory;   
                     when others => case start_writing is
                    when '0' => Next_state <=Waiting_for_data;
                    when others => Next_state <=Idle; 
               end case;
          end case;
     when Waiting_for_data => case tc_50_clk_cnt is
          when '1' => Next_state <=Write_Memory;
          when others => Next_state <=Waiting_for_data; 
     end case;
     when Write_Memory => Next_state <= Idle;
     when Read_Memory  => Next_state <= Load_REG;
     when Load_REG => Next_state <=Wait_Bit_Time;
     when Wait_Bit_Time => case tc_bittime_clk_cnt is
          when '1' => Next_state <=Shift_Data_Out;
          when others => Next_state <=Wait_Bit_Time;
     end case;
     when Shift_Data_Out => case tc_10_bit_cnt is
          when '0' => Next_state <=Wait_Bit_Time;
          when others => case tc_memsize_data_cnt is
               when '0' => Next_state <=Read_memory;
               when others => Next_state <=Idle;
          end case;
     end case;
     end case;
     end if;
     end process Next_state_evaluation;
     


     state_transition: process(clk)
      begin
          if rising_edge(clk) then
          present_state <= Next_state;
          end if; 
     end process state_transition;
          
          output_decode: process(present_state , UART_rx , start_writing , tc_10_bit_cnt) 
          begin
          
          --default output
          en_addr_cnt <='0';
          upn_down_addr_cnt <='0';
          PISO_load <='0';
          PISO_shift <='0';
          rstn_bit_cnt <='1';
          en_bit_cnt <='0';
          rstn_clk_cnt <='1';
          en_clk_cnt <='0';
          rstn_data_cnt <='1';
          en_data_cnt <='0';
          rdn_wr_data_ssram <='0';
          UART_tx_mux_sel <='0';
          
          case present_state is
               when Idle => 
                    rstn_clk_cnt <='0'; 
                    rstn_data_cnt <='0'; 
                    if UART_rx='1' then 
                         if start_writing='0' then 
                         en_addr_cnt <='1';
                          end if; 
                    end if;
          
          when Waiting_for_data=>
                en_clk_cnt <='1';
          
          when Write_Memory=> 
               rdn_wr_data_ssram <='1';
          
          when Read_Memory=> 
               en_addr_cnt <='1'; 
               upn_down_addr_cnt <='1';
               rstn_clk_cnt <='0';
               rstn_bit_cnt <='0';
          
          when Load_REG=>
                PISO_load <='1';
          when Wait_Bit_Time=> 
               en_clk_cnt <='1'; 
               UART_tx_mux_sel <='1';
          when Shift_Data_out=> 
               PISO_shift <='1'; 
               en_bit_cnt <='1';
               rstn_clk_cnt <='0'; 
               UART_tx_mux_sel <='1'; 
               if tc_10_bit_cnt ='1' then
                     en_data_cnt <='1'; 
               end if;
          end case;
     end process output_decode;
          
end architecture behavioral;