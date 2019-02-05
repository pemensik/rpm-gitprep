= gitprep =

== Legacy replacement of %patchX ==
To use git to prepare your rpm sources, install this package and add into your ~/.rpmmacros:

```
%_fixperms %{_gitprep_fixperms}
%__patch %{_gitprep__patch}
```

Now, after you do rpmbuild -bp X.spec or fedpkg prep, you have prepared changes in source directory as git
repo.

All %patch1, %patch2 would now be done using git, without additional modification of spec file.

Commit messages may contain original patch name in commit notes . But git diff <path> to list patches changing subtree can be used.
Or use gitk to review what patches did to your sources.

== autopatch ==

Support for autopatch were added. It is now possible to use it with macro:

```
%autosetup -S gitprep -N
...
%autopatch
```

It would mark commits with original patch name, patch number. If commit was originally output of git format-patch, commit message would be intact.
