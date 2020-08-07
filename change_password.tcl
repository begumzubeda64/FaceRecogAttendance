#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Aug 07, 2020 10:31:39 PM IST  platform: Windows NT
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
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 629x466+650+150
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
    wm title $top "Attendance - Change Password"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra45 \
        -borderwidth 2 -relief groove -background #00ffff -height 455 \
        -width 605 
    vTcl:DefineAlias "$top.fra45" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra45
    label $site_3_0.lab46 \
        -background #00ffff -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text {Old Password} 
    vTcl:DefineAlias "$site_3_0.lab46" "Label1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent47 \
        -background white -borderwidth 2 -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 314 
    vTcl:DefineAlias "$site_3_0.ent47" "txtOld" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activebackground #f9f9f9 -activeforeground black -background #00ffff \
        -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {New Password} 
    vTcl:DefineAlias "$site_3_0.lab48" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent49 \
        -background white -borderwidth 2 -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 314 
    vTcl:DefineAlias "$site_3_0.ent49" "txtNew" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #eac515 -borderwidth 3 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Change 
    vTcl:DefineAlias "$site_3_0.but50" "btnChange" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab46 \
        -in $site_3_0 -x 0 -relx 0.11 -y 0 -rely 0.191 -width 0 \
        -relwidth 0.251 -height 0 -relheight 0.102 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent47 \
        -in $site_3_0 -x 0 -relx 0.41 -y 0 -rely 0.191 -width 314 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.11 -y 0 -rely 0.382 -width 0 \
        -relwidth 0.251 -height 0 -relheight 0.102 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent49 \
        -in $site_3_0 -x 0 -relx 0.41 -y 0 -rely 0.382 -width 314 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but50 \
        -in $site_3_0 -x 0 -relx 0.41 -y 0 -rely 0.552 -width 316 -relwidth 0 \
        -height 63 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra45 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.008 -height 0 \
        -relheight 1.011 -anchor nw -bordermode ignore 
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

