#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Mar 30, 2021 03:41:29 PM IST  platform: Windows NT
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




proc vTclWindow.top63 {base} {
    global vTcl
    if {$base == ""} {
        set base .top63
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
    wm title $top "Attendance - Edit Subject"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra64 \
        -borderwidth 2 -relief groove -background #00ffff -height 595 \
        -width 725 
    vTcl:DefineAlias "$top.fra64" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra64
    label $site_3_0.lab65 \
        -background #00ffff -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text {Subject Name} 
    vTcl:DefineAlias "$site_3_0.lab65" "Label1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent66 \
        -background white -borderwidth 2 -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 344 
    vTcl:DefineAlias "$site_3_0.ent66" "txtSubName" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab67 \
        -activebackground #f9f9f9 -activeforeground black -background #00ffff \
        -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Class Name} 
    vTcl:DefineAlias "$site_3_0.lab67" "Label1_5" vTcl:WidgetProc "Toplevel1" 1
    ttk::combobox $site_3_0.tCo68 \
        \
        -font {-family {Yu Gothic UI Semibold} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -textvariable combobox -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$site_3_0.tCo68" "comboCls" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but69 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #eac515 -borderwidth 3 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Save 
    vTcl:DefineAlias "$site_3_0.but69" "btnEditSub" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab65 \
        -in $site_3_0 -x 0 -relx 0.132 -y 0 -rely 0.217 -width 0 \
        -relwidth 0.225 -height 0 -relheight 0.092 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent66 \
        -in $site_3_0 -x 0 -relx 0.359 -y 0 -rely 0.232 -width 0 \
        -relwidth 0.49 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab67 \
        -in $site_3_0 -x 0 -relx 0.12 -y 0 -rely 0.388 -width 0 \
        -relwidth 0.24 -height 0 -relheight 0.091 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tCo68 \
        -in $site_3_0 -x 0 -relx 0.359 -y 0 -rely 0.403 -width 0 \
        -relwidth 0.498 -height 0 -relheight 0.072 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but69 \
        -in $site_3_0 -x 0 -relx 0.37 -y 0 -rely 0.556 -width 353 -relwidth 0 \
        -height 63 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra64 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.004 -height 0 \
        -relheight 1.012 -anchor nw -bordermode ignore 
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
Window show .top63 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
