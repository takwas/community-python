var gulp = require('gulp');
var sass = require('gulp-sass');
var browserSync = require('browser-sync');
var exec = require('child_process').exec;

gulp.task('styles', function() {
    gulp.src('./admin/resources/sass/**/*.scss')
        .pipe(sass({outputStyle: 'compressed'})
            .on('error', sass.logError))
        .pipe(gulp.dest('./admin/static/css/'));

    gulp.src('./auth/resources/sass/**/*.scss')
        .pipe(sass({outputStyle: 'compressed'})
            .on('error', sass.logError))
        .pipe(gulp.dest('./auth/static/css/'));
});

gulp.task('connect-sync', function () {
    browserSync.init({
        notify: false,
        port: 5000,
        proxy: 'localhost:5000'
    })

    // TODO: reload on py files
    gulp.watch(['**/*.html','**/*.scss']).on('change', function () {
        browserSync.reload();
    });
});

gulp.task('default', ['styles', 'connect-sync'], function() {
    gulp.watch('./admin/resources/sass/**/*.scss',['styles']);
    gulp.watch('./register/resources/sass/**/*.scss',['styles']);
});
