
########## Enthalpy vs Polar Counts ##########

H <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)

#set vectors#

H.p <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)
P <- c(1,1,0,1,7,5,2,2,9,11,12,16,11,11,10,11,5,12,11,10,12,11,12,12,3,4,10,4,10,11,8,9,3,7,1,5,4,14,10,1,1,4,1,6,7,5,4,7,10,8,2,9,12,13,14,8,7,8,8,6,8,7,3,4,8,5,2,10,6,6,3,6,7,3,3,8,6,4,10,9,0,14,11,1,1,1,7,5,4,6,8,8,4,4,4,1,9,9,12,10,4,6,11)

#Plot#
plot(P,H.p, 
pch=1, col="#009999",
xlim=c(0,20), ylim=c(-110,50), 
main="Enthalpy vs Polar Counts",
xlab="Polar Counts",ylab="Enthalpy(kJ/mol)")

grid(NULL ,lwd = 1) # grid 

#Regression#
lm.HP <- lm(H.p~P) 

#Line of best fit#
abline(lm.HP, col="#cc6699") 

#Data points and Summary (print out)#


H.p
P

summary(lm.HP)

########## Enthalpy vs Apolar Counts ##########

#set vectors#

H.ap <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)
AP <- c(9,7,7,8,44,48,20,36,51,65,75,103,72,62,80,66,53,69,66,69,79,68,72,68,41,27,52,31,71,94,83,78,37,75,49,17,60,93,63,50,27,39,9,30,30,51,70,70,24,28,24,31,80,70,126,40,61,61,57,46,56,70,20,34,42,56,22,58,33,59,74,45,47,26,20,60,57,66,36,38,6,99,80,33,22,81,76,78,86,49,58,62,49,18,24,31,42,46,84,71,23,19,57)

#Plot#
plot(AP,H.ap, 
pch=1, col="#009999",
xlim=c(0,150), ylim=c(-120,50), 
main="Enthalpy vs Apolar Counts",
xlab="Apolar Counts",ylab="Enthalpy(kJ/mol)")

grid(NULL ,lwd = 1) # grid 

#Regression#
lm.HAP <- lm(H.ap~AP) 

#Line of best fit#
abline(lm.HAP, col="#cc6699") 

#Data points and Summary (print out)#

H.ap
AP

summary(lm.HAP)


########## Enthalpy vs Binding Water Counts ##########

#set vectors#
H.bw <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)
BW <- c(3,5,6,4,18,10,3,6,6,7,5,8,7,7,8,4,10,7,6,9,7,9,11,6,6,5,6,3,14,12,14,11,6,18,4,12,22,8,7,2,2,10,4,5,13,11,22,20,7,4,9,11,5,9,8,7,9,6,10,9,6,7,4,8,11,8,6,13,15,35,17,7,16,11,10,10,9,13,1,3,3,10,8,0,2,9,0,2,4,2,6,19,12,5,10,15,2,10,6,8,5,6,4)

#Plot#
plot(BW,H.bw, 
pch=1, col="#009999",
xlim=c(0,35), ylim=c(-120,50), 
main="Enthalpy vs Binding Water Counts",
xlab="Binding Water Counts",ylab="Enthalpy(kJ/mol)")

grid(NULL ,lwd = 1) # grid 

#Regression#
lm.HBW <- lm(H.bw~BW)

#Line of best fit#
abline(lm.HBW, col="#cc6699") 

#Data points and Summary (print out)#
H.bw
BW

summary(lm.HBW)
############################################

########## Enthalpy vs Change In Polar Water Contacts ##########
#H.pwc <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)
#PWC <- c(-7,-2,-1,-11,-54,-37,-15,-19,-47,-49,-57,-68,-53,-53,-47,-55,-39,-63,-56,-56,-55,-59,-60,-46,-30,-13,-49,-19,-91,-81,-66,-76,-26,-45,-10,-75,-156,-80,-51,-14,-14,-35,-15,-27,-49,-52,-47,-55,-29,-25,-22,-40,-53,-57,-63,-32,-39,-31,-27,-42,-40,-37,-19,-25,-47,-32,-18,-56,-50,-77,-44,-41,-44,-24,-23,-44,-47,-43,-22,-26,-3,-72,-45,-10,-8,-19,-34,-27,-24,-24,-21,-48,-45,-10,-28,-37,-26,-48,-56,-63,-15,-32,-54)

#***** Absolute Loss of Polar Contacts *****#
H.pwc <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)
PWC <- c(7,2,1,11,54,37,15,19,47,49,57,68,53,53,47,55,39,63,56,56,55,59,60,46,30,13,49,19,91,81,66,76,26,45,10,75,156,80,51,14,14,35,15,27,49,52,47,55,29,25,22,40,53,57,63,32,39,31,27,42,40,37,19,25,47,32,18,56,50,77,44,41,44,24,23,44,47,43,22,26,3,72,45,10,8,19,34,27,24,24,21,48,45,10,28,37,26,48,56,63,15,32,54)
#********************#

#Plot#
plot(PWC,H.pwc, 
pch=4, col="#009999",
xlim=c(0,160), ylim=c(-120,50), 
main="Enthalpy vs Loss in Polar Water Contacts",
xlab="Loss of Polar Water Contacts",ylab="Enthalpy(kJ/mol)")

grid(NULL ,lwd = 1) # grid

#Regression#
lm.HPWC <- lm(H.pwc~PWC)

#Line of best fit#
abline(lm.HPWC, col="#cc6699") 

#Data points and Summary (print out)#
H.pwc
PWC

summary(lm.HPWC)
##########

########## Enthalpy vs Change In Apolar Water Contacts ##########
#H.apwc <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)
#APWC <- c(-2,-5,-5,-18,-85,-71,-65,-53,-49,-67,-91,-92,-84,-71,-84,-69,-45,-82,-68,-78,-84,-81,-77,-79,-55,-24,-55,-26,-78,-88,-100,-102,-60,-94,-84,-40,-87,-77,-59,-84,-67,-34,-26,-46,-58,-125,-151,-133,-44,-23,-52,-51,-79,-80,-90,-55,-58,-52,-51,-65,-78,-70,-35,-69,-55,-86,-60,-47,-65,-195,-132,-52,-43,-51,-44,-48,-63,-164,-29,-29,-22,-83,-58,-45,-41,-75,-68,-68,-77,-54,-44,-128,-125,-5,-33,-51,-25,-53,-86,-63,-22,-35,-47)

#***** Absolute Loss of Apolar Contacts *****#
H.ap <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)
APWC <- c(2,5,5,18,85,71,65,53,49,67,91,92,84,71,84,69,45,82,68,78,84,81,77,79,55,24,55,26,78,88,100,102,60,94,84,40,87,77,59,84,67,34,26,46,58,125,151,133,44,23,52,51,79,80,90,55,58,52,51,65,78,70,35,69,55,86,60,47,65,195,132,52,43,51,44,48,63,164,29,29,22,83,58,45,41,75,68,68,77,54,44,128,125,5,33,51,25,53,86,63,22,35,47)
#********************#

#Plot#
plot(APWC,H.apwc, 
pch=4, col="#009999",
xlim=c(0,200), ylim=c(-120,50), 
main="Enthalpy vs Loss in Apolar Water Contacts",
xlab="Loss of Apolar Water Contacts",ylab="Enthalpy(kJ/mol)")

grid(NULL ,lwd = 1) # grid

#Regression#
lm.HAPWC <- lm(H.apwc~APWC)

#Line of best fit#
abline(lm.HAPWC, col="#cc6699") 

#Data points and Summary (print out)#
H.apwc
APWC

summary(lm.HAPWC)
##########


############### Add P and AP ###############

### Summary of the model ###
summary(lm(H ~ AP + P))

######################### 3D #########################


library(ggplot2)
install.packages("rgl")
library(rgl)

Enthalpy <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)

P <- c(1,1,0,1,7,5,2,2,9,11,12,16,11,11,10,11,5,12,11,10,12,11,12,12,3,4,10,4,10,11,8,9,3,7,1,5,4,14,10,1,1,4,1,6,7,5,4,7,10,8,2,9,12,13,14,8,7,8,8,6,8,7,3,4,8,5,2,10,6,6,3,6,7,3,3,8,6,4,10,9,0,14,11,1,1,1,7,5,4,6,8,8,4,4,4,1,9,9,12,10,4,6,11)
AP <- c(9,7,7,8,44,48,20,36,51,65,75,103,72,62,80,66,53,69,66,69,79,68,72,68,41,27,52,31,71,94,83,78,37,75,49,17,60,93,63,50,27,39,9,30,30,51,70,70,24,28,24,31,80,70,126,40,61,61,57,46,56,70,20,34,42,56,22,58,33,59,74,45,47,26,20,60,57,66,36,38,6,99,80,33,22,81,76,78,86,49,58,62,49,18,24,31,42,46,84,71,23,19,57)

##### R Graphics Cookbook, Ch13, p286-287 - Set up the matrix #####
# Given a model, predict zvar from xvar and yvar
# Defaults to range of x and y variables, and a 16x16 grid
predictgrid <- function(model, xvar, yvar, zvar, res = 16, type = NULL) {
  # Find the range of the predictor variable. This works for lm and glm
  # and some others, but may require customization for others.
  xrange <- range(model$model[[xvar]])
  yrange <- range(model$model[[yvar]])

  newdata <- expand.grid(x = seq(xrange[1], xrange[2], length.out = res),
                         y = seq(yrange[1], yrange[2], length.out = res))
  names(newdata) <- c(xvar, yvar)
  newdata[[zvar]] <- predict(model, newdata = newdata, type = type)
  newdata
}


# Convert long-style data frame with x, y, and z vars into a list
# with x and y as row/column values, and z as a matrix.
df2mat <- function(p, xvar = NULL, yvar = NULL, zvar = NULL) {
  if (is.null(xvar)) xvar <- names(p)[1]
  if (is.null(yvar)) yvar <- names(p)[2]
  if (is.null(zvar)) zvar <- names(p)[3]

  x <- unique(p[[xvar]])
  y <- unique(p[[yvar]])
  z <- matrix(p[[zvar]], nrow = length(y), ncol = length(x))

  m <- list(x, y, z)
  names(m) <- c(xvar, yvar, zvar)
  m
}

# Function to interleave the elements of two vectors
interleave <- function(v1, v2)  as.vector(rbind(v1,v2))

########## END #########

#Generate the linear model
model <- lm(Enthalpy ~ AP + P)

#Get predicted values from Gibbs from AP and P
pred_Enthalpy <-predict(model)

#Get predicted mpg from a grid of wt and disp
mpgrid_df <- predictgrid(model, "AP", "P", "Enthalpy")
mpgrid_list <- df2mat(mpgrid_df)

# Make the plot with the data points
plot3d(AP, P, Enthalpy, type="s", size=0.7, lit=FALSE)

# Add the corresponding predicted points (smaller)
spheres3d(AP, P, pred_Enthalpy, alpha=0.1, type="s", size=0.5, lit=FALSE)

# Add line segments showing the error
segments3d(
interleave(AP,AP),
interleave(P,P),
interleave(Enthalpy,pred_Enthalpy),
alpha=0.4, col="red"
)

# Add the mesh of predicted values
surface3d(mpgrid_list$AP, mpgrid_list$P, mpgrid_list$Enthalpy,
alpha=0.4, front="lines", back="lines")


########## FINAL GRAPH ##########
plot3d(
AP, P, Enthalpy, 
main="3D Plot of Enthalpy vs Apolar and Polar Counts",
xlab="", ylab="", zlab="",
axes=FALSE,

type="s", size=0.75, lit=FALSE,
)

# Add the corresponding predicted points (smaller)
spheres3d(AP, P, pred_Enthalpy, alpha=0.1, type="s", size=0.5, lit=FALSE)

# Add line segments showing the error
segments3d(
interleave(AP,AP),
interleave(P,P),
interleave(Enthalpy,pred_Enthalpy),
alpha=0.4, col="purple"
)

# Add the mesh of predicted values
surface3d(mpgrid_list$AP, mpgrid_list$P, mpgrid_list$Enthalpy,
alpha=0.4, front="lines", back="lines")

#Draw the box

rgl.bbox(
color="grey50",emission="grey50",
xlen=0, ylen=0, zlen=0
)

#set default color of future objects to black

rgl.material(color="black")

#Add axes to specific sides

axes3d(edges=c("x--","y+-","z--"),
ntick=8, #attempt 10 tick marks per side
cex=0.75 #smaller font
)

#Add axes labels
mtext3d("Apolar Counts", edge="x--", line=2) # line = how far set label from axis
mtext3d("Polar Counts", edge="y+-", line=3)
mtext3d("Enthalpy(kJ/mol)", edge="z--", line=3)

### Summary of the model ###
summary(lm(Enthalpy ~ AP + P))

#play3d(spin3d())

###########################################################################################################

########## PACKAGES TO FETCH ##########
library(ggplot2)
install.packages("rgl")
library(rgl)
#######################################

########## Loss in Polar and Apolar Water Contacts 3D ##########
#Enthalpy <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)
#PWC <- c(-7,-2,-1,-11,-54,-37,-15,-19,-47,-49,-57,-68,-53,-53,-47,-55,-39,-63,-56,-56,-55,-59,-60,-46,-30,-13,-49,-19,-91,-81,-66,-76,-26,-45,-10,-75,-156,-80,-51,-14,-14,-35,-15,-27,-49,-52,-47,-55,-29,-25,-22,-40,-53,-57,-63,-32,-39,-31,-27,-42,-40,-37,-19,-25,-47,-32,-18,-56,-50,-77,-44,-41,-44,-24,-23,-44,-47,-43,-22,-26,-3,-72,-45,-10,-8,-19,-34,-27,-24,-24,-21,-48,-45,-10,-28,-37,-26,-48,-56,-63,-15,-32,-54)
#APWC <- c(-2,-5,-5,-18,-85,-71,-65,-53,-49,-67,-91,-92,-84,-71,-84,-69,-45,-82,-68,-78,-84,-81,-77,-79,-55,-24,-55,-26,-78,-88,-100,-102,-60,-94,-84,-40,-87,-77,-59,-84,-67,-34,-26,-46,-58,-125,-151,-133,-44,-23,-52,-51,-79,-80,-90,-55,-58,-52,-51,-65,-78,-70,-35,-69,-55,-86,-60,-47,-65,-195,-132,-52,-43,-51,-44,-48,-63,-164,-29,-29,-22,-83,-58,-45,-41,-75,-68,-68,-77,-54,-44,-128,-125,-5,-33,-51,-25,-53,-86,-63,-22,-35,-47)

#***** Absolute Loss of Water Contacts *****#
Enthalpy <- c(-21.34,-17.99,-29.71,-22.59,-15.06,-41.8,-28.33,-61.5,11.655,7.9,14.6,20.6,20.5,14.1,22,16.6,-14.015,8.1,8.9,17.3,20.7,7.7,11.4,24.6,-22.8,-18.9,-38.03,-18.9,-45.94,-37.36,-34.43,-34.98,-111.29,-102.93,-21.75,-5.785,-5.785,-2.51,-20.84,-53.2,-48.7,-17.18,-19.7,-29.9,-2.51,-32.22,8.79,-21.965,-46.32,-31.18,-18.74,-74.59,20.1,11.3,29.3,-20.6,-39.6,-32.9,-34.4,-24.7,-57.8,-37,-73.22,-74.265,-14.015,-39.6,-25.31,-13.81,-58.99,8.315,6.28,-13.39,-14.015,-29.29,-6.28,-96.23,-99.16,10.88,-31,-26.44,-80.92,36,22.4,-47.89,-44.54,-32.22,7.11,5.36,9,-56.905,-29.46,-41.84,-29.29,-77.8,-28.72,-30.4,-46.65,-14.015,39.4,9.75,-18.9,-40.795,-31.97)
PWC <- c(7,2,1,11,54,37,15,19,47,49,57,68,53,53,47,55,39,63,56,56,55,59,60,46,30,13,49,19,91,81,66,76,26,45,10,75,156,80,51,14,14,35,15,27,49,52,47,55,29,25,22,40,53,57,63,32,39,31,27,42,40,37,19,25,47,32,18,56,50,77,44,41,44,24,23,44,47,43,22,26,3,72,45,10,8,19,34,27,24,24,21,48,45,10,28,37,26,48,56,63,15,32,54)
APWC <- c(2,5,5,18,85,71,65,53,49,67,91,92,84,71,84,69,45,82,68,78,84,81,77,79,55,24,55,26,78,88,100,102,60,94,84,40,87,77,59,84,67,34,26,46,58,125,151,133,44,23,52,51,79,80,90,55,58,52,51,65,78,70,35,69,55,86,60,47,65,195,132,52,43,51,44,48,63,164,29,29,22,83,58,45,41,75,68,68,77,54,44,128,125,5,33,51,25,53,86,63,22,35,47)
#********************#

##### R Graphics Cookbook, Ch13, p286-287 - Set up the matrix #####
# Given a model, predict zvar from xvar and yvar
# Defaults to range of x and y variables, and a 16x16 grid
predictgrid <- function(model, xvar, yvar, zvar, res = 16, type = NULL) {
  # Find the range of the predictor variable. This works for lm and glm
  # and some others, but may require customization for others.
  xrange <- range(model$model[[xvar]])
  yrange <- range(model$model[[yvar]])

  newdata <- expand.grid(x = seq(xrange[1], xrange[2], length.out = res),
                         y = seq(yrange[1], yrange[2], length.out = res))
  names(newdata) <- c(xvar, yvar)
  newdata[[zvar]] <- predict(model, newdata = newdata, type = type)
  newdata
}


# Convert long-style data frame with x, y, and z vars into a list
# with x and y as row/column values, and z as a matrix.
df2mat <- function(p, xvar = NULL, yvar = NULL, zvar = NULL) {
  if (is.null(xvar)) xvar <- names(p)[1]
  if (is.null(yvar)) yvar <- names(p)[2]
  if (is.null(zvar)) zvar <- names(p)[3]

  x <- unique(p[[xvar]])
  y <- unique(p[[yvar]])
  z <- matrix(p[[zvar]], nrow = length(y), ncol = length(x))

  m <- list(x, y, z)
  names(m) <- c(xvar, yvar, zvar)
  m
}

# Function to interleave the elements of two vectors
interleave <- function(v1, v2)  as.vector(rbind(v1,v2))

########## END #########

#Generate the linear model
model <- lm(Enthalpy ~ APWC + PWC)

#Get predicted values from Enthalpy from AP and P
pred_Enthalpy <-predict(model)

#Get predicted mpg from a grid of wt and disp
mpgrid_df <- predictgrid(model, "APWC", "PWC", "Enthalpy")
mpgrid_list <- df2mat(mpgrid_df)

# Make the plot with the data points
plot3d(APWC, PWC, Enthalpy, type="s", size=0.7, lit=FALSE)

# Add the corresponding predicted points (smaller)
spheres3d(APWC, PWC, pred_Enthalpy, alpha=0.1, type="s", size=0.5, lit=FALSE)

# Add line segments showing the error
segments3d(
interleave(APWC,APWC),
interleave(PWC,PWC),
interleave(Enthalpy,pred_Enthalpy),
alpha=0.4, col="red"
)

# Add the mesh of predicted values
surface3d(mpgrid_list$APWC, mpgrid_list$PWC, mpgrid_list$Enthalpy,
alpha=0.4, front="lines", back="lines")


########## FINAL GRAPH ##########
plot3d(
APWC,PWC, Enthalpy, 
main="3D Plot of Enthalpy vs Loss in Apolar and Polar Water Contacts",
xlab="", ylab="", zlab="",
axes=FALSE,

type="s", size=0.75, lit=FALSE,
)

# Add the corresponding predicted points (smaller)
spheres3d(APWC, PWC, pred_Enthalpy, alpha=0.1, type="s", size=0.5, lit=FALSE)

# Add line segments showing the error
segments3d(
interleave(APWC,APWC),
interleave(PWC,PWC),
interleave(Enthalpy,pred_Enthalpy),
alpha=0.4, col="blue"
)

# Add the mesh of predicted values
surface3d(mpgrid_list$APWC, mpgrid_list$PWC, mpgrid_list$Enthalpy,
alpha=0.4, front="lines", back="lines")

#Draw the box

rgl.bbox(
color="grey50",emission="grey50",
xlen=0, ylen=0, zlen=0
)

#set default color of future objects to black

rgl.material(color="black")

#Add axes to specific sides

axes3d(edges=c("x--","y+-","z--"),
ntick=8, #attempt 10 tick marks per side
cex=0.70 #smaller font
)

#Add axes labels
mtext3d("Loss of Apolar Water Contacts", edge="x--", line=2) # line = how far set label from axis
mtext3d("Loss of Polar Water Contacts", edge="y+-", line=3)
mtext3d("Enthalpy(kJ/mol)", edge="z--", line=4)

### Summary of the model ###
summary(lm(Enthalpy ~ APWC + PWC))



