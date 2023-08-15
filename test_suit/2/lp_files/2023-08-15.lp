\* Source Pyomo model name=Model *\

min 
objective:
+0 ONE_VAR_CONSTANT

s.t.

c_e_BusBlock_balance(bel_0_0)_:
+1 flow(conversion_bel_0_0)
-1 flow(bel_sink_el_0_0)
= 0

c_e_BusBlock_balance(com_3_0_0)_:
-1 flow(com_3_conversion_0_0)
= -1

c_e_BusBlock_balance(com_2_0_0)_:
-1 flow(com_2_conversion_0_0)
= -1

c_e_BusBlock_balance(com_1_0_0)_:
-1 flow(com_1_conversion_0_0)
= -1

c_e_TransformerBlock_relation(conversion_com_3_bel_0_0)_:
-0.3 flow(conversion_bel_0_0)
+1 flow(com_3_conversion_0_0)
= 0

c_e_TransformerBlock_relation(conversion_com_2_bel_0_0)_:
-0.2 flow(conversion_bel_0_0)
+1 flow(com_2_conversion_0_0)
= 0

c_e_TransformerBlock_relation(conversion_com_1_bel_0_0)_:
-0.1 flow(conversion_bel_0_0)
+1 flow(com_1_conversion_0_0)
= 0

bounds
   1 <= ONE_VAR_CONSTANT <= 1
   0 <= flow(conversion_bel_0_0) <= +inf
   0 <= flow(bel_sink_el_0_0) <= +inf
   0 <= flow(com_3_conversion_0_0) <= +inf
   0 <= flow(com_2_conversion_0_0) <= +inf
   0 <= flow(com_1_conversion_0_0) <= +inf
end
