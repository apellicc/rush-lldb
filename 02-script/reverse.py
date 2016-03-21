import lldb

def ft_reverse(debugger, command, result, dict):
	print 'FT_' + str(lldb.SBDebugger.GetSelectedTarget(debugger))[::-1]

lldb.debugger.HandleCommand('command script add -f reverse.ft_reverse reverse')
