#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Aug 09, 2020 07:12:28 PM IST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 722x588+650+150
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Attendance - Add Student"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra45 \
        -borderwidth 2 -relief groove -background #00ffff -height 615 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 745 
    vTcl:DefineAlias "$top.fra45" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra45
    label $site_3_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black -background #00ffff \
        -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Student Name} 
    vTcl:DefineAlias "$site_3_0.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent46 \
        -background white -borderwidth 2 -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 384 
    vTcl:DefineAlias "$site_3_0.ent46" "txtName" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab47 \
        -activebackground #f9f9f9 -activeforeground black -background #00ffff \
        -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Student Class} 
    vTcl:DefineAlias "$site_3_0.lab47" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo50 \
        -values {{Select Class}} \
        -font {-family {Yu Gothic UI Semibold} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -state readonly -textvariable combobox -foreground {} -background {} \
        -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo50" "comboClass" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #eac515 -borderwidth 3 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Take Picture} 
    vTcl:DefineAlias "$site_3_0.but51" "btnTakePic" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black -background #00ffff \
        -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Student Picture} 
    vTcl:DefineAlias "$site_3_0.lab52" "Label1_4" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #eac515 -borderwidth 3 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Add 
    vTcl:DefineAlias "$site_3_0.but53" "btnAdd" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #eac515 -borderwidth 3 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Browse Picture} 
    vTcl:DefineAlias "$site_3_0.but56" "btnBrowsePic" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab46 \
        -activebackground #f9f9f9 -activeforeground black -background #00ffff \
        -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$site_3_0.lab46" "lblPicPath" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activebackground #f9f9f9 -activeforeground black -background #00ffff \
        -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Roll No} 
    vTcl:DefineAlias "$site_3_0.lab48" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent49 \
        -background white -borderwidth 2 -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 384 
    vTcl:DefineAlias "$site_3_0.ent49" "txtRoll" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab45 \
        -in $site_3_0 -x 0 -relx 0.11 -y 0 -rely 0.251 -width 0 \
        -relwidth 0.23 -height 0 -relheight 0.075 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent46 \
        -in $site_3_0 -x 0 -relx 0.359 -y 0 -rely 0.251 -width 384 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.081 -y 0 -rely 0.374 -width 0 \
        -relwidth 0.271 -height 0 -relheight 0.075 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo50 \
        -in $site_3_0 -x 0 -relx 0.362 -y 0 -rely 0.374 -width 0 \
        -relwidth 0.519 -height 0 -relheight 0.076 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but51 \
        -in $site_3_0 -x 0 -relx 0.362 -y 0 -rely 0.52 -width 166 -relwidth 0 \
        -height 53 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.107 -y 0 -rely 0.52 -width 0 \
        -relwidth 0.231 -height 0 -relheight 0.075 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but53 \
        -in $site_3_0 -x 0 -relx 0.362 -y 0 -rely 0.699 -width 386 \
        -relwidth 0 -height 53 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but56 \
        -in $site_3_0 -x 0 -relx 0.631 -y 0 -rely 0.52 -width 186 -relwidth 0 \
        -height 53 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 0 -relx 0.376 -y 0 -rely 0.618 -width 0 \
        -relwidth 0.501 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.11 -y 0 -rely 0.134 -width 0 \
        -relwidth 0.23 -height 0 -relheight 0.075 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent49 \
        -in $site_3_0 -x 0 -relx 0.359 -y 0 -rely 0.134 -width 384 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra45 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.004 -height 0 \
        -relheight 1.015 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

