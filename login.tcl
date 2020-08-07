#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Aug 04, 2020 06:42:17 PM IST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { \
    login_pro_jpg "../../xampp/htdocs/AttendanceFace/Images/login_pro.jpg" \
}
vTcl:create_project_images $image_list   ;# In image.tcl


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
        -background #00ffff 
    wm focusmodel $top passive
    wm geometry $top 814x644+650+150
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
    wm title $top "Attendance Login"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra48 \
        -borderwidth 2 -relief groove -background #00ffff -height 1013 \
        -width 1916 
    vTcl:DefineAlias "$top.fra48" "FrameLogin" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra48
    button $site_3_0.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image login_pro_jpg -pady 0 -relief groove -text Button 
    vTcl:DefineAlias "$site_3_0.but51" "icon" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab52 \
        -background #00ffff -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -text Username 
    vTcl:DefineAlias "$site_3_0.lab52" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black -background #00ffff \
        -disabledforeground #a3a3a3 \
        -font {-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Password 
    vTcl:DefineAlias "$site_3_0.lab53" "Label2" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent54 \
        -background #ffffffffffff -disabledforeground #a3a3a3 \
        -font {-family Arial -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 254 
    vTcl:DefineAlias "$site_3_0.ent54" "txtUser" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent55 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family Arial -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 254 
    vTcl:DefineAlias "$site_3_0.ent55" "txtPass" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #eac515 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Login 
    vTcl:DefineAlias "$site_3_0.but56" "btnLogin" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #eac515 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI Emoji} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Cancel 
    vTcl:DefineAlias "$site_3_0.but57" "btnCancel" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but51 \
        -in $site_3_0 -x 0 -relx 0.167 -y 0 -rely 0.039 -width 166 \
        -relwidth 0 -height 193 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.084 -y 0 -rely 0.306 -width 0 \
        -relwidth 0.069 -height 0 -relheight 0.036 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 0 -relx 0.084 -y 0 -rely 0.375 -width 0 \
        -relwidth 0.069 -height 0 -relheight 0.036 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent54 \
        -in $site_3_0 -x 0 -relx 0.209 -y 0 -rely 0.306 -width 254 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent55 \
        -in $site_3_0 -x 0 -relx 0.209 -y 0 -rely 0.375 -width 254 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but56 \
        -in $site_3_0 -x 0 -relx 0.078 -y 0 -rely 0.484 -width 206 \
        -relwidth 0 -height 53 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but57 \
        -in $site_3_0 -x 0 -relx 0.235 -y 0 -rely 0.484 -width 206 \
        -relwidth 0 -height 53 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra48 \
        -in $top -x 0 -y 0 -width 0 -relwidth 2.354 -height 0 \
        -relheight 1.573 -anchor nw -bordermode ignore 
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
