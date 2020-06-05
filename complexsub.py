import tkinter as tk
import numpy as np

class Game_Init(tk.Tk):
    game_delay = 100
    view_size = 800
    display_size = 300
    bota_x = 450
    bota_y = 450
    display_pad_y = -130
    display_pad_x = 20
    clock_increments = 1
    clock_num = 1
    clock_max = 1000
    real_clock_denum = 1
    imag_clock_denum = 1
    imag_clock_num_scalar = 1
    real_clock_num_scalar = 1
    real_t_num = 1
    real_t_denum = 1
    imag_t_num = 1
    imag_t_denum = 1
    unit_ball_drop = 1
    micro_ball_drop = 0
    mega_ball_drop = 0
    val_power = 0
    val_decimal_power = 10 ** val_power
    positive_negative = 1
    clock_max_temp = 10
    clock_increments_temp = 1
    val_power_temp = 1
    real_clock_num_scalar_temp = 10
    real_clock_denum_temp = 10
    real_t_num_temp = 10
    real_t_denum_temp = 10
    imag_clock_num_scalar_temp = 10
    imag_clock_denum_temp = 10
    imag_t_num_temp = 10
    imag_t_denum_temp = 10
    unit_ball_drop_temp = 10
    micro_ball_drop_temp = 10
    mega_ball_drop_temp = 10
    positive_negative_temp = 1
    def __init__(self):
        super().__init__()
        self.bind("<Key>", self.key_pressed)
        self.tk_frame = tk.Canvas(self, width=self.view_size, height=self.view_size-150) 
        self.tk_frame.pack()
        self.timer_clock()
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
    def timer_clock(self): 
        self.tk_frame.delete(tk.ALL) 
        self.animate_dots()
        self.display_stats()
        self.clock_num += self.clock_increments
        if self.clock_num >= self.clock_max:
            self.clock_num = 1
        self.tk_frame.after(self.game_delay, self.timer_clock)
    def animate_dots(self):
        for i in range(int(self.unit_ball_drop)):
            self.bota_real = (np.real(np.e**-(1j*np.pi*(self.real_t_num/self.real_t_denum)*(((self.clock_num*self.real_clock_num_scalar)/self.real_clock_denum)-(self.clock_max/2))))*self.display_size)+450
            self.bota_imag = (np.imag(np.e**-(1j*np.pi*(self.imag_t_num/self.imag_t_denum)*(((self.clock_num*self.imag_clock_num_scalar)/self.imag_clock_denum)-(self.clock_max/2))))*self.display_size)+450
            self.tk_frame.create_oval(self.display_pad_x+self.bota_real, self.display_pad_y+self.bota_imag, self.display_pad_x+self.bota_real+10, self.display_pad_y+self.bota_imag+10, fill="yellow")
            self.botb_real = (np.real(np.e**-(1j*np.pi*(self.real_t_num/self.real_t_denum)*(((((self.clock_num-i)*self.real_clock_num_scalar)+(self.val_decimal_power*1))/self.real_clock_denum)-(self.clock_max/2))))*self.display_size)+450
            self.botb_imag = (np.imag(np.e**-(1j*np.pi*(self.imag_t_num/self.imag_t_denum)*(((((self.clock_num-i)*self.imag_clock_num_scalar)+(self.val_decimal_power*1))/self.imag_clock_denum)-(self.clock_max/2))))*self.display_size)+450
            self.tk_frame.create_oval(self.display_pad_x+self.botb_real, self.display_pad_y+self.botb_imag, self.display_pad_x+self.botb_real+10, self.display_pad_y+self.botb_imag+10, fill="green")
            self.botc_real = (np.real(np.e**-(1j*np.pi*(self.real_t_num/self.real_t_denum)*(((((self.clock_num+i)*self.real_clock_num_scalar)-(self.val_decimal_power*1))/self.real_clock_denum)-(self.clock_max/2))))*self.display_size)+450
            self.botc_imag = (np.imag(np.e**-(1j*np.pi*(self.imag_t_num/self.imag_t_denum)*(((((self.clock_num+i)*self.imag_clock_num_scalar)-(self.val_decimal_power*1))/self.imag_clock_denum)-(self.clock_max/2))))*self.display_size)+450
            self.tk_frame.create_oval(self.display_pad_x+self.botc_real, self.display_pad_y+self.botc_imag, self.display_pad_x+self.botc_real+10, self.display_pad_y+self.botc_imag+10, fill="green")
        for i in range(int(self.mega_ball_drop)):
            self.botd_real = (np.real(np.e**-(1j*np.pi*(self.real_t_num/self.real_t_denum)*((((self.clock_num*self.real_clock_num_scalar)*(1000*i))/self.real_clock_denum)-(self.clock_max/2))))*self.display_size)+450
            self.botd_imag = (np.imag(np.e**-(1j*np.pi*(self.imag_t_num/self.imag_t_denum)*((((self.clock_num*self.imag_clock_num_scalar)*(1000*i))/self.imag_clock_denum)-(self.clock_max/2))))*self.display_size)+450
            self.tk_frame.create_oval(self.display_pad_x+self.botd_real, self.display_pad_y+self.botd_imag, self.display_pad_x+self.botd_real+10, self.display_pad_y+self.botd_imag+10, fill="red")
        for i in range(int(self.micro_ball_drop)):
            self.bote_real = (np.real(np.e**-(1j*np.pi*(self.real_t_num/self.real_t_denum)*((((self.clock_num*self.real_clock_num_scalar)*(.001*i))/self.real_clock_denum)-(self.clock_max/2))))*self.display_size)+450
            self.bote_imag = (np.imag(np.e**-(1j*np.pi*(self.imag_t_num/self.imag_t_denum)*((((self.clock_num*self.imag_clock_num_scalar)*(.001*i))/self.imag_clock_denum)-(self.clock_max/2))))*self.display_size)+450
            self.tk_frame.create_oval(self.display_pad_x+self.bote_real,self.display_pad_y+self.bote_imag, self.display_pad_x+self.bote_real+10, self.display_pad_y+self.bote_imag+10, fill="blue")
    def display_stats(self):
        self.tk_frame.create_text(60, 20, text='clock_max(e)', fill="red")   
        self.tk_frame.create_text(60, 40, text=self.clock_max, fill="red")    
        self.tk_frame.create_text(60, 60, text='increments(c)', fill="red")   
        self.tk_frame.create_text(60, 80, text=self.clock_increments, fill="red")   
        self.tk_frame.create_text(60, 100, text='val_power(q/z)', fill="red")   
        self.tk_frame.create_text(60, 120, text=self.val_power+1, fill="red")
        self.tk_frame.create_text(60, 140, text='real_clock_num(s)', fill="green")   
        self.tk_frame.create_text(60, 160, text=self.real_clock_num_scalar, fill="green")  
        self.tk_frame.create_text(60, 180, text='real_clock_denum(down)', fill="green")   
        self.tk_frame.create_text(60, 200, text=self.real_clock_denum, fill="green")
        self.tk_frame.create_text(60, 220, text='real_t_num(d)', fill="green")   
        self.tk_frame.create_text(60, 240, text=self.real_t_num, fill="green")
        self.tk_frame.create_text(60, 260, text='real_t_denum(right)', fill="green")   
        self.tk_frame.create_text(60, 280, text=self.real_t_denum, fill="green")
        self.tk_frame.create_text(60, 300, text='imag_clock_num_scala(w)', fill="purple")   
        self.tk_frame.create_text(60, 320, text=self.imag_clock_num_scalar, fill="purple")  
        self.tk_frame.create_text(60, 340, text='imag_clock_denum(up)', fill="purple")   
        self.tk_frame.create_text(60, 360, text=self.imag_clock_denum, fill="purple")
        self.tk_frame.create_text(60, 380, text='imag_t_num(a)', fill="purple")   
        self.tk_frame.create_text(60, 400, text=self.imag_t_num, fill="purple")
        self.tk_frame.create_text(60, 420, text='imag_t_denum(left)', fill="purple")   
        self.tk_frame.create_text(60, 440, text=self.imag_t_denum, fill="purple") 
        self.tk_frame.create_text(60, 460, text='mega_ball_drop(r)', fill="black")   
        self.tk_frame.create_text(60, 480, text=self.mega_ball_drop, fill="blue")  
        self.tk_frame.create_text(60, 500, text='unit_ball_drop(g)', fill="black")   
        self.tk_frame.create_text(60, 520, text=self.unit_ball_drop, fill="green")   
        self.tk_frame.create_text(60, 540, text='micro_ball_drop(v)', fill="black")   
        self.tk_frame.create_text(60, 560, text=self.micro_ball_drop, fill="red")
        self.tk_frame.create_text(60, 580, text='positive or negative(f)', fill="black")   
        self.tk_frame.create_text(60, 600, text=self.positive_negative, fill="red")
    def key_pressed(self, tk_command):
        
        self.tk_frame = tk_command.widget.tk_frame
        
        if tk_command.keysym == "f": 
            self.positive_negative = self.positive_negative*-1
        
        if tk_command.keysym == "Up" and self.imag_clock_denum >= 1:
            self.imag_clock_denum += (self.positive_negative*self.val_decimal_power)
        if tk_command.keysym == "w"and self.imag_clock_denum >= 1:
            self.imag_clock_num_scalar += (self.positive_negative*self.val_decimal_power)
        if tk_command.keysym == "Down" and self.real_clock_denum >= 1:
            self.real_clock_denum += (self.positive_negative*self.val_decimal_power)
        if tk_command.keysym == "s" and self.real_clock_num_scalar >= 1:
            self.real_clock_num_scalar += (self.positive_negative*self.val_decimal_power)
        if tk_command.keysym == "Left" and self.imag_t_denum >= 1:
            self.imag_t_denum += (self.positive_negative*self.val_decimal_power)
        if tk_command.keysym == "a" and self.imag_t_num >= 1: 
            self.imag_t_num += (self.positive_negative*self.val_decimal_power)
        if tk_command.keysym == "Right" and self.real_t_denum >= 1: 
            self.real_t_denum += (self.positive_negative*self.val_decimal_power)
        if tk_command.keysym == "d" and self.real_t_num >= 1:
            self.real_t_num += (self.positive_negative*self.val_decimal_power)
                
        if tk_command.keysym == "b":
            self.clock_num =  1
            
        if tk_command.keysym == "q":
            self.val_power +=  1
            self.val_decimal_power = 10 ** self.val_power
            
        if tk_command.keysym == "z":
            self.val_power -=  1
            self.val_decimal_power = 10 ** self.val_power
            
        if tk_command.keysym == "e":
            self.clock_max += self.positive_negative*self.val_decimal_power
        if tk_command.keysym == "c":
            self.clock_increments += self.positive_negative*self.val_decimal_power
            
        if tk_command.keysym == "g" and self.val_decimal_power >= 1:
            self.unit_ball_drop += self.positive_negative*self.val_decimal_power
        if tk_command.keysym == "v" and self.val_decimal_power >= 1:
            self.micro_ball_drop += self.positive_negative*self.val_decimal_power
        if tk_command.keysym == "r" and self.val_decimal_power >= 1:
            self.mega_ball_drop += self.positive_negative*self.val_decimal_power
            
        if tk_command.keysym == "t":
            self.bota_x = 450
            self.bota_y = 450
            self.clock_num = 1
            self.clock_max = 1000
            self.clock_increments = 1
            self.real_clock_denum = 1
            self.imag_clock_denum = 1
            self.imag_clock_num_scalar = 1
            self.real_clock_num_scalar = 1
            self.real_t_num = 1
            self.real_t_denum = 1
            self.imag_t_num = 1
            self.imag_t_denum = 1
            self.unit_ball_drop = 1
            self.micro_ball_drop = 0
            self.mega_ball_drop = 0
            self.val_power = 0  
            self.val_decimal_power = 10 ** self.val_power  
            self.positive_negative = 1        
        if tk_command.keysym == "y":
            self.bota_x = 450
            self.bota_y = 450
            self.clock_num = 1
            self.clock_max = 100
            self.clock_increments = .1
            self.real_clock_denum = 1
            self.imag_clock_denum = 1
            self.imag_clock_num_scalar = 1
            self.real_clock_num_scalar = 1
            self.real_t_num = 1
            self.real_t_denum = 1
            self.imag_t_num = 1
            self.imag_t_denum = 1
            self.unit_ball_drop = 1
            self.micro_ball_drop = 0
            self.mega_ball_drop = 0
            self.val_power = 0  
            self.val_decimal_power = 10 ** self.val_power  
            self.positive_negative = 1
        if tk_command.keysym == "n":
            self.bota_x = 450
            self.bota_y = 450
            self.clock_num = 1
            self.clock_max = 10
            self.clock_increments = .01
            self.real_clock_denum = 1
            self.imag_clock_denum = 1
            self.imag_clock_num_scalar = 1
            self.real_clock_num_scalar = 1
            self.real_t_num = 1
            self.real_t_denum = 1
            self.imag_t_num = 1
            self.imag_t_denum = 1
            self.unit_ball_drop = 1
            self.micro_ball_drop = 0
            self.mega_ball_drop = 0
            self.val_power = 0  
            self.val_decimal_power = 10 ** self.val_power  
            self.positive_negative = 1
        if tk_command.keysym == "m":
            self.bota_x = 450
            self.bota_y = 450
            self.clock_num = 1
            self.clock_max = 10
            self.clock_increments = .01
            self.real_clock_denum = 1
            self.imag_clock_denum = 1
            self.imag_clock_num_scalar = 1
            self.real_clock_num_scalar = 1
            self.real_t_num = 1
            self.real_t_denum = 1
            self.imag_t_num = 1
            self.imag_t_denum = 1
        if tk_command.keysym == "u":
            self.clock_max = 1000
            self.clock_increments = 1
            self.real_clock_denum = 11
            self.imag_clock_denum = 6
            self.imag_clock_num_scalar = 5
            self.real_clock_num_scalar = 5
            self.real_t_num = 7
            self.real_t_denum = 3
            self.imag_t_num = 1
            self.imag_t_denum = 1
            self.unit_ball_drop = 2
            self.micro_ball_drop = 10
            self.mega_ball_drop = 20
            self.val_power = 1
            self.val_decimal_power = 10 ** self.val_power  
            self.positive_negative = 1        
        if tk_command.keysym == "i":
            self.clock_max = 1000
            self.clock_increments = 1.01
            self.val_power = 1
            self.real_clock_num_scalar = 1
            self.real_clock_denum = 2
            self.real_t_num = 1
            self.real_t_denum = 2
            self.imag_clock_num_scalar = 1
            self.imag_clock_denum = 2
            self.imag_t_num = 1
            self.imag_t_denum = 2
            self.unit_ball_drop = 10
            self.micro_ball_drop = 10
            self.mega_ball_drop = 10
            self.val_decimal_power = 10 ** self.val_power  
            self.positive_negative = 1       
        if tk_command.keysym == "o":
            self.clock_max = 1000
            self.clock_increments = 1.01
            self.val_power = 1
            self.real_clock_num_scalar = 1
            self.real_clock_denum = 2
            self.real_t_num = 1
            self.real_t_denum = 2.01
            self.imag_clock_num_scalar = 1
            self.imag_clock_denum = 2.01
            self.imag_t_num = 1
            self.imag_t_denum = 2
            self.unit_ball_drop = 10
            self.micro_ball_drop = 10
            self.mega_ball_drop = 10
            self.val_decimal_power = 10 ** self.val_power  
            self.positive_negative = 1   
        if tk_command.keysym == "p":
            self.clock_max = 1000
            self.clock_increments = 1
            self.val_power = 0
            self.real_clock_num_scalar = 54
            self.real_clock_denum = 25
            self.real_t_num = 13
            self.real_t_denum = 28
            self.imag_clock_num_scalar = 3
            self.imag_clock_denum = 414
            self.imag_t_num = 2
            self.imag_t_denum = 4
            self.unit_ball_drop = 49
            self.micro_ball_drop = 80
            self.mega_ball_drop = 70
            self.val_decimal_power = 10 ** self.val_power  
            self.positive_negative = 1  
        if tk_command.keysym == "l":
            self.clock_max = 1011
            self.clock_increments = 1
            self.val_power = 0
            self.real_clock_num_scalar = 7
            self.real_clock_denum = 10
            self.real_t_num = 1
            self.real_t_denum = 32
            self.imag_clock_num_scalar = 27
            self.imag_clock_denum = 19
            self.imag_t_num = 22
            self.imag_t_denum = 31
            self.unit_ball_drop = 47
            self.micro_ball_drop = 72
            self.mega_ball_drop =47
            self.val_decimal_power = 10 ** self.val_power  
            self.positive_negative = 1       
        if tk_command.keysym == "j":
            self.clock_max_temp = self.clock_max
            self.clock_increments_temp = self.clock_increments
            self.val_power_temp = self.val_power
            self.real_clock_num_scalar_temp = self.real_clock_num_scalar
            self.real_clock_denum_temp = self.real_clock_denum
            self.real_t_num_temp = self.real_t_num
            self.real_t_denum_temp = self.real_t_denum
            self.imag_clock_num_scalar_temp = self.imag_clock_num_scalar
            self.imag_clock_denum_temp = self.imag_clock_denum
            self.imag_t_num_temp = self.imag_t_num
            self.imag_t_denum_temp = self.imag_t_denum
            self.unit_ball_drop_temp = self.unit_ball_drop
            self.micro_ball_drop_temp = self.micro_ball_drop
            self.mega_ball_drop_temp = self.mega_ball_drop
            self.positive_negative_temp = self.positive_negative   
        if tk_command.keysym == "k":
            self.clock_max = self.clock_max_temp
            self.clock_increments = self.clock_increments_temp
            self.val_power = self.val_power_temp
            self.real_clock_num_scalar = self.real_clock_num_scalar_temp
            self.real_clock_denum = self.real_clock_denum_temp
            self.real_t_num = self.real_t_num_temp
            self.real_t_denum = self.real_t_denum_temp
            self.imag_clock_num_scalar = self.imag_clock_num_scalar_temp
            self.imag_clock_denum = self.imag_clock_denum_temp
            self.imag_t_num = self.imag_t_num_temp
            self.imag_t_denum = self.imag_t_denum_temp
            self.unit_ball_drop = self.unit_ball_drop_temp
            self.micro_ball_drop = self.micro_ball_drop_temp
            self.mega_ball_drop = self.mega_ball_drop_temp
            self.positive_negative = self.positive_negative_temp   
            
init_grid = Game_Init()
init_grid.mainloop()