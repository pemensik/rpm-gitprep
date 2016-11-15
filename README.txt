To use git to prepare your rpm sources, install this package and add into your ~/.rpmmacros:

%_fixperms %{_gitprep_fixperms}
%__patch %{_gitprep__patch}

Now, after you do rpmbuild -bp X.spec or fedpkg prep, you have prepared changes in source directory as git
repo. Commit messages are not very helpful now. But you can use git diff <path> to list patches changing subtree.
Or use gitk to review what patches did to your sources.
