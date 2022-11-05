#1. CREATE ABOVE DICTIONARY USING BASIC METHOD 
#{} AND NAME IT AS score_vk_basic
score_vk = {
        'one_day' : 700,
        'test ': 740,
        't_20 ': 470,
        'international' : 250
}
print(score_vk)
print('---------------------------------')

score_vk_basic=dict(one_day=700,test = 740,t_20 = 470,international =250)
print(score_vk_basic)

print('-------------------------------------------')
#2. CREATE ABOVE DICTIONARY USING variable assignments way AND NAME IT AS score_vk_var
score_vk_var_tup=dict([('one_day',700),('test',740),('t_20',470),('international',250)])
print(score_vk_var_tup)

print('-------------------------------------------')
#3. CREATE ABOVE DICTIONARY USING#tuple pair way  AND NAME IT AS score_vk_basic_tup

keylist=['one_day','test','t_20','international']
values=[700,740,470,250]

score_vk_basic_tup=dict(zip(keylist,values))
print(score_vk_basic_tup)