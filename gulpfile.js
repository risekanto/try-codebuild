var gulp = require('gulp'),
    gft = require('gulp-file-tree');
 
// var tree = require('tree');

gulp.task('default', function () {
	// console.log(tree);
    // return gulp.src('/Users/kanto/git/morecon.jp/data/class/*.*')
    // return gulp.src('/Users/kanto/git/morecon.jp/data/**/*.*')
    return gulp.src('./**/*.*')
        .pipe(gft())
        .pipe(gulp.dest('./'));
});
