# Create Line Chart

# convert factor to numeric for convenience
ntrees <- 3

# get the range for the x and y axis
xrange <-c(1,2,3)
names <- c("gzip", "bzip2", "xz")
#yrange <- range(10,1400)

y1 <- c(220, 360, 1340)
y2<-  c(71,245, 520)
y3<-  c(221, 395, 670)


# set up the plot
plot(xrange, ylim=c(10,1400), type="n", 
     ylab="Time in Seconds", xlab="", xaxt ="n" )
colors <- rainbow(ntrees)
linetype <- c(1:ntrees)
plotchar <- seq(18,18+ntrees,1)
axis(1, at=1:3, lab=names)

# add lines
for (i in 1:ntrees) {
  if (i==1) {
  lines(y1, type="b", lwd=1.5,
        lty=linetype[i], col=colors[i], pch=plotchar[i])
  }else{
    if (i==2) {
    lines(y2, type="b", lwd=1.5,
          lty=linetype[i], col=colors[i], pch=plotchar[i])
    } else{
      lines(y3, type="b", lwd=1.5,
            lty=linetype[i], col=colors[i], pch=plotchar[i]) 
    }
  }
}

# add a title and subtitle
#title("Tree Growth", "example of line plot")

# add a legend
legend(xrange[1], 1300,  c("Original", "Only Custom Format", "Custom Format + Overhead from our tool"), cex=0.8, col=colors,
       pch=plotchar, lty=linetype, bty="n")