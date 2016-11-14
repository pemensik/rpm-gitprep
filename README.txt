To use git to prepare your rpm sources, install this package and add into your ~/.rpmmacros:

%_fixperms %{_gitprep_fixperms}
%__patch %{_gitprep__patch}

